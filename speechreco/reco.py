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

CODE_STRS = ["coding", "environment", "intialize"]
for phrase in CODE_STRS:
	if phrase in text:
		speak("Okay, preparing your coding workspace!")
		web.open('https://github.com/byfelipesanchez')
		web.open('https://leetcode.com/')
		os.startfile('C:\\WINDOWS\\system32\\cmd')
		os.startfile('C:\\Program Files\\Sublime Text 3\\sublime_text')
		os.startfile('C:\\Users\\2018f\\AppData\\Local\\GitHubDesktop\\GitHubDesktop')


STY_STRS = ["prepare for studying", "study", "studying"]
for phrase in STY_STRS:
	if phrase in text:
		speak("Okay, preparing your studying workspace!")
		web.open("https://www.youtube.com/")
		web.open("https://calendar.google.com/calendar/u/0/r/month")
		web.open('https://docs.google.com/spreadsheets/d/1gKKb8IRe0FVfm2NfwSBisoC40DZ-mnH26hXoWqtoUHY/edit#gid=0')




