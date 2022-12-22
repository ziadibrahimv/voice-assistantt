import subprocess
import wolframalpha
import pyttsx3
import tkinter
import wikipedia
import json
import random
import operator
import speech_recognition as sr
import datetime
from time import ctime
import webbrowser
import os
import pyjokes
import smtplib
import pywhatkit as kit
import ctypes
import time
import requests
import pywhatkit
import shutil
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')



def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning!")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon!")

	else:
		speak("Good Evening!")

	speak("I am your voice Assistant, how can i help you")

	


	

def takeCommand():
	
	r = sr.Recognizer()
	with sr.Microphone() as source:

		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)
		query = ''
	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except sr.UnknownValueError:
		speak("Unable to Recognize your voice.")
	except sr.RequestError:
		speak("sorry my speech service is down")
	return query


if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()
	wishMe()
	
	while True:
		
		query = takeCommand().lower()
		

		if 'find in wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("find in wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)


		elif 'open youtube' in query:
			speak("Here you go to youtube\n")
			webbrowser.open("youtube.com")

		elif 'open youtube' in query:
			query = query.replace("open youtube","")
			Query = query.replace(" ","+")
			speak("Here is your request on youtube")
			webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

		elif 'open google' in query:
			speak("Here you go to Google\n")
			webbrowser.open("google.com")

		elif 'how are you' in query:
			speak("I am fine, Thank you")

		elif 'tell a joke' in query:
			speak(pyjokes.get_joke())

		elif 'convert background' in query:
			ctypes.windll.user32.SystemParametersInflow(20,0,'C:/Users/ea/OneDrive/Desktop/images.JPG',0)
			speak("Background changed successfully")




		elif 'what is time' in query:
			speak(ctime())

		elif 'find location' in query:
			location = takeCommand('Find location')
			url = 'https://www.google.com/maps' + location + '/&amp;'
			webbrowser.get().open(url)
			speak('here is the location of' + location)

		elif "open word" in query: 
			speak("opening word")
			os.startfile("C:/Users/ea/OneDrive/Desktop/test.docx")
        


		elif 'I am good' in query:
			speak("It's good to know that your fine")


		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()


		

		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "")
			query = query.replace("play", "")		
			webbrowser.open(query)

		elif "who i am" in query:
			speak("If you talk then definitely your human.")



		elif "who are you" in query:
			speak("I am your virtual assistant")



    
		elif 'lock window' in query:
				speak("locking the device")
				ctypes.windll.user32.LockWorkStation()

		elif 'shutdown system' in query:
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f')
				

		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop jarvis from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)

		elif "convert voice" in query:
			speak("do you want the voice to be male or female?")
			gender = takeCommand()
			print(gender)
			genderIndex = 1
			if gender == 'female':
				genderIndex = 1
			engine.setProperty('voice',voices[genderIndex].id)
			speak("Voice changed successfully, what else can I help you with")





		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
			

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])



