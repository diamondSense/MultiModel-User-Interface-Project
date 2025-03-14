# Test for text recognition model using Google TTS (text to speech)

from gtts import gTTS
import os

text = "Test to check if text to speech works perfectly or not, this library needs to be connected to the internet to work"

tts = gTTS(text, lang='en')
tts.save("test/test_TTS.mp3")

os.system("start test/test_TTS.mp3")
