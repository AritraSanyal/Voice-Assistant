import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from googlesearch import search
import pyjokes

engine = pyttsx3.init()
engine.say("I will speak this text")
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)