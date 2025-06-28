from flask import Flask, request
from flask_sock import Sock
import asyncio
from utils import elevenlabs_stt_stream, elevenlabs_tts_stream
from langchain.chains import ConversationalRetrievalQA
from langchain.memory import ConversationBufferMemory
from chromadb import PersistentClient
import openai
import os

app = Flask(__name__)
sock = Sock(app)

db = PersistentClient("./chroma")
retriever = db.get_or_create_collection("docs").as_retriever()
qa = ConversationalRetrievalQA.from_llm(
    llm=openai.ChatCompletion(model="gpt-4o-mini"),
    retriever=retriever,
    memory=ConversationBufferMemory(return_messages=True)
)

@sock.route('/chat')
def chat(ws):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tts_stream = None
    while True:
        data = ws.receive()
        if data is None:
            break
        # Assume data is raw audio bytes
        text = loop.run_until_complete(elevenlabs_stt_stream(data))
        if getattr(text, 'final', False):
            answer = qa({"question": text.text})["answer"]
            ws.send({"type": "answer", "text": answer})
            tts_stream = elevenlabs_tts_stream(answer)
            for chunk in tts_stream:
                ws.send(chunk)