from __future__ import print_function
from gtts import gTTS
import os
import datetime
import playsound
import speech_recognition as sr
import subprocess
import webbrowser as web
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import requests
import bs4
import gspread
from bs4 import BeautifulSoup
import datetime
import smtplib, ssl
from subprocess import call
# https://developers.google.com/calendar/quickstart/python

# SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

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
			print("Exception" + str(e))

	return said

text = get_audio()


# def request():
#     r = requests.get('https://br.financas.yahoo.com/quote/KLBN4.SA?p=KLBN4.SA&.tsrc=fin-srch')
#     soup = bs4.BeautifulSoup(r.text, 'lxml')
#     return soup


# def parse(soup):
#         date = datetime.datetime.now()
#         name = soup.find('h1', class_ = 'D(ib) Fz(18px)').text.strip()
#         price = soup.find_all('div', {'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
#         total = {'date':date, 'name': name ,'price':price}
#         return total


# def output(total):
#         gc = gspread.service_account(filename='creds.json')
#         sh = gc.open('Stocks').sheet1
#         sh.append_row([str(total['date']), str(total['name']), str(total['price'])])

# data = request()
# total = parse(data)
# output(total)
# print(total)

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


# def authenticate_google():
#     """Shows basic usage of the Google Calendar API.
#     Prints the start and name of the next 10 events on the user's calendar.
#     """
#     creds = None
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)

#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)

#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)

#     service = build('calendar', 'v3', credentials=creds)

#     return service


# def get_events(n, service):
#     # Call the Calendar API
#     now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
#     print(f'Getting the upcoming {n} events')
#     events_result = service.events().list(calendarId='primary', timeMin=now,
#                                         maxResults=n, singleEvents=True,
#                                         orderBy='startTime').execute()
#     events = events_result.get('items', [])

#     if not events:
#         print('No upcoming events found.')
#     for event in events:
#         start = event['start'].get('dateTime', event['start'].get('date'))
#         print(start, event['summary'])


# service = authenticate_google()
# get_events(2, service)



