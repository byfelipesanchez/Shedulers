import os
import datetime
import playsound
import speech_recognition as sr
from gtts import gTTS
import subprocess
import webbrowser as web


print("Hello, Let's get started!")

def speak(text):
	tts = gTTS(text=text, lang='en')
	filename = "voice.mp3"
	tts.save(filename)
	playsound.playsound(filename)


def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

		try:
			said = r.recognize_google(audio)
			print(said)
		except Exception as e:
			print("exception: " + str(e))

	return said

text = get_audio()

# TALK_STRS = ["hello","start coding environment", "prepare for coding", "i am gonna programm", "intialize coding environment"]

if "hello" or "start coding environment" or "prepare for coding" or "i am gonna programm" or "intialize coding environment" in text:
	speak("Okay, intializing your coding workspace! This will take just a second...")
	os.startfile('C:\\Program Files\\Sublime Text 3\\sublime_text')
	speak("All Done!")
# speak("hello felipe, how are you doing")