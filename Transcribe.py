from faster_whisper import WhisperModel

AUDIO_FILE = "recordings/voice.wav"

print("🧠 Loading Whisper model...")

model = WhisperModel(
    "tiny",
    device="cpu",
    compute_type="int8"
)

print("🎧 Transcribing your recording...")

segments, info = model.transcribe(AUDIO_FILE)

transcription = ""

for segment in segments:
    transcription += segment.text + " "

print("\n📝 TRANSCRIPTION:")
print(transcription.strip())
