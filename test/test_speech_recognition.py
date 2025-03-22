# Test for speech recognition model using Whisper (speech to text)
# https://openai.com/index/whisper/
# import whisper

# # Change models for better reuslts (small model detect correctly and is much faster)
# model = whisper.load_model("small")
# result = model.transcribe("test/recording1.wav")
# print(result["text"])

# Test with live audio and assitant response
import whisper
import sounddevice as sd
import numpy as np
import time
import soundfile as sf
from gtts import gTTS
import os

# Load Whisper model
model = whisper.load_model("small")

# Audio recording settings
RATE = 16000  # Whisper prefers 16kHz
CHUNK = 1024
SILENCE_THRESHOLD = 100  # Lower = more sensitive to sound
SILENCE_DURATION = 1.5  # Time in seconds to wait before stopping

# Helper function to detect silence
def is_silent(audio_chunk):
    """Check if the audio is silent (low volume)."""
    return np.abs(audio_chunk).mean() < SILENCE_THRESHOLD

def speak(text):
    """Convert text to speech and play it using sounddevice."""
    tts = gTTS(text=text, lang="en")
    tts.save("response.mp3")

    # Load and play the saved audio file
    data, samplerate = sf.read("response.mp3")
    sd.play(data, samplerate)
    sd.wait()  # Wait until playback finishes
    os.remove("response.mp3")  # Clean up file

def listen():
    """Listen continuously and transcribe when user stops speaking."""
    print("Listening...")

    while True:
        audio_frames = []
        silence_counter = 0
        recording = False

        with sd.InputStream(samplerate=RATE, channels=1, dtype="int16") as stream:
            while True:
                data, _ = stream.read(CHUNK)  # Read live audio
                audio_chunk = np.frombuffer(data, dtype=np.int16)

                if not is_silent(audio_chunk):
                    if not recording:
                        recording = True

                    audio_frames.append(audio_chunk)
                    silence_counter = 0  # Reset silence counter
                elif recording:
                    silence_counter += CHUNK / RATE  # Convert chunk size to seconds
                    if silence_counter > SILENCE_DURATION:
                        break  # Stop recording

        if not audio_frames:
            continue  # If no speech detected, keep listening

        # Convert recorded audio to NumPy array
        audio_data = np.concatenate(audio_frames, axis=0).astype(np.float32) / 32768.0  # Convert int16 → float32


        # Transcribe speech using Whisper
        result = model.transcribe(audio_data)
        user_text = result["text"].strip()

        if not user_text:
            print("No transcription detected, retrying...")
            continue  # Skip empty transcriptions

        print(f"You: {user_text}")

        # Process user command
        if "recipe" in user_text.lower():
            bot_response = "Sure! What recipe do you need help with?"
        elif "temperature" in user_text.lower():
            bot_response = "The best temperature for baking a cake is 350 degrees Fahrenheit."
        elif "timer" in user_text.lower():
            bot_response = "Okay, setting a timer for 10 minutes!"
        elif "thank you" in user_text.lower():
            bot_response = "You're welcome! Happy cooking!"
        else:
            bot_response = "Sorry, I didn't understand that. Can you repeat?"

        print(f"Assistant: {bot_response}")
        speak(bot_response)  # Speak the response

try:
    listen()
except KeyboardInterrupt:
    print("\nStopping...")


