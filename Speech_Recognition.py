import speech_recognition as sr
import webbrowser as wb
# import gttks
import pyttsx3
import os
import sys

engine = pyttsx3.init()

def talk(words):
	print(words)
	engine.say(words)
	engine.runAndWait()

talk("Привет, спроси у меня что-либо")

def command():
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("Говорите")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)

	try:
		cmd = r.recognize_google(audio, language="ru-RU").lower()
		print("User said: " + cmd)
	except sr.UnknownValueError:
		talk("Я вас не поняла")
		cmd = command()

	return cmd

def make_something(cmd):
	if 'открой сайт' in cmd:
		wb.open("google.com")
	elif 'привет' in cmd:
		talk("Привет привет")
	elif 'стоп' in cmd:
		talk("Досвидания")
		sys.exit()


while True:
	make_something(command())
