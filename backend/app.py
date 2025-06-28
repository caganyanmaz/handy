from flask import Flask, request
from flask_sock import Sock
import asyncio
from utils import elevenlabs_stt_stream, elevenlabs_tts_stream
import os

app = Flask(__name__)
sock = Sock(app)

@app.route('/')
def health_check():
    return {"status": "ok", "message": "Handy AI Assistant Backend is running"}

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
            # Simple response for now - you can enhance this later
            answer = f"I heard you say: '{text.text}'. This is a test response using ElevenLabs voice features."
            ws.send({"type": "answer", "text": answer})
            tts_stream = elevenlabs_tts_stream(answer)
            for chunk in tts_stream:
                ws.send(chunk)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)