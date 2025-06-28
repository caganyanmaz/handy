import os
import requests
import json
import asyncio
from typing import AsyncGenerator, Generator

# ElevenLabs API configuration
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
ELEVENLABS_BASE_URL = "https://api.elevenlabs.io/v1"

# Async helper for ElevenLabs streaming STT
async def elevenlabs_stt_stream(audio_bytes):
    """Convert audio bytes to text using ElevenLabs STT API"""
    if not ELEVENLABS_API_KEY:
        # Fallback to dummy if no API key
        class DummySTT:
            text = "This is a dummy transcript."
            final = True
        return DummySTT()
    
    try:
        headers = {
            "xi-api-key": ELEVENLABS_API_KEY
        }
        
        # Use ElevenLabs STT endpoint
        url = f"{ELEVENLABS_BASE_URL}/speech-to-text"
        
        # Prepare multipart form data with required model_id
        files = {
            'file': ('audio.wav', audio_bytes, 'audio/wav')
        }
        data = {
            'model_id': 'scribe_v1'
        }
        
        response = requests.post(
            url,
            headers=headers,
            files=files,
            data=data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            class Transcript:
                text = result.get('text', '')
                final = True
            return Transcript()
        else:
            print(f"ElevenLabs STT error: {response.status_code} - {response.text}")
            # Fallback to dummy
            class DummySTTError:
                text = "Sorry, I couldn't understand that."
                final = True
            return DummySTTError()
            
    except Exception as e:
        print(f"Error in ElevenLabs STT: {e}")
        # Fallback to dummy
        class DummySTTException:
            text = "Sorry, there was an error processing your speech."
            final = True
        return DummySTTException()

# Generator for ElevenLabs TTS streaming
def elevenlabs_tts_stream(text, voice_id="21m00Tcm4TlvDq8ikWAM"):  # Default voice: Rachel
    """Convert text to speech using ElevenLabs TTS API"""
    if not ELEVENLABS_API_KEY:
        # Fallback to dummy if no API key
        for _ in range(3):
            yield b"dummy audio chunk"
        return
    
    try:
        headers = {
            "xi-api-key": ELEVENLABS_API_KEY,
            "Content-Type": "application/json"
        }
        
        data = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }
        
        # Use ElevenLabs TTS endpoint
        url = f"{ELEVENLABS_BASE_URL}/text-to-speech/{voice_id}/stream"
        
        response = requests.post(
            url,
            headers=headers,
            json=data,
            stream=True,
            timeout=30
        )
        
        if response.status_code == 200:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    yield chunk
        else:
            print(f"ElevenLabs TTS error: {response.status_code} - {response.text}")
            # Fallback to dummy
            for _ in range(3):
                yield b"dummy audio chunk"
                
    except Exception as e:
        print(f"Error in ElevenLabs TTS: {e}")
        # Fallback to dummy
        for _ in range(3):
            yield b"dummy audio chunk" 