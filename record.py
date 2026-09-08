import sounddevice as sd
import numpy as np
import wave

DURATION = 10
SAMPLE_RATE = 16000
FILENAME = "recordings/voice.wav"

print("🎤 Recording will start now...")
print(f"Speak for {DURATION} seconds.")

audio = sd.rec(
    int(DURATION * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="int16"
)

sd.wait()

with wave.open(FILENAME, "wb") as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(SAMPLE_RATE)
    wav_file.writeframes(audio.tobytes())

print(f"Recording saved to {FILENAME}")
