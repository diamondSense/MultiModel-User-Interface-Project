# Test for speech recognition model (speech to text )
import whisper

# Change models for better reuslts (small model detect correctly and is much faster)
model = whisper.load_model("small")
result = model.transcribe("test/recording1.wav")
print(result["text"])

