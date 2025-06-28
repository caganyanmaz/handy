import os

# Async helper for ElevenLabs streaming STT
async def elevenlabs_stt_stream(audio_bytes):
    # TODO: Implement ElevenLabs STT streaming API call
    # For now, return a dummy object with .text and .final
    class Dummy:
        text = "This is a dummy transcript."
        final = True
    return Dummy()

# Generator for ElevenLabs TTS streaming
def elevenlabs_tts_stream(text):
    # TODO: Implement ElevenLabs TTS streaming API call
    # For now, yield dummy audio bytes
    for _ in range(3):
        yield b"dummy audio chunk" 