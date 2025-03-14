# Test for speech recognition model using Whisper (speech to text)
# https://openai.com/index/whisper/
import whisper

# Change models for better reuslts (small model detect correctly and is much faster)
model = whisper.load_model("small")
result = model.transcribe("test/recording1.wav")
print(result["text"])

