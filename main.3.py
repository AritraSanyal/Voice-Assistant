import datetime
import speech_recognition as sr
import os
import time
import wikipedia
import webbrowser
from googlesearch import search


# THIS FUNCTION IS TO CONVERT THE TEXT INTO SPEECH
# I USED THIS AND NOT PYTTSX3 'CAUSE THERE WAS SOME ERROR SHOWING IN THAT MODULE
def speak(textf):
    os.system(f"say {textf}")


# THIS FUNCTION IS FOR CONVERTING THE SPEECH TO TEXT
# OR SIMPLY TO LISTEN WHAT THE USER HAS SAID
def take_command():
    print("Listening...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source=source)
        audio = r.listen(source)
        try:
            print("Recognising...")
            queryinfunc = r.recognize_google(audio, language="en-in")
            print(f"User said: {queryinfunc}")
            return queryinfunc
        except Exception:
            return "Please say that again..."


# THIS FUNCTION IS TO WISH THE USER WHEN THE PROGRAM IS INITIATED
def wishme():
    timenow = time.strftime("%H", time.localtime())
    timenow = int(timenow)
    if 0 <= timenow <= 5:
        print("Good morning sir..., though its dark outside")
        speak("Good morning sir..., though its dark outside")
        # print("Its pretty late i think you should fall asleep")
        # speak("Its pretty late i think you should fall asleep")
        # print(
        #     "If you are up such late at night, you must have some important things to do! I will help with any thing you need.")
        # speak(
        #     "If you are up such late at night, you must have some important things to do! I will help with any thing you need.")
    elif 5 < timenow <= 11:
        print("Good morning sir...")
        speak("Good morning sir...")
    elif 12 <= timenow <= 17:
        print("Good afternoon sir...")
        speak("Good afternoon sir...")
    elif 17 < timenow < 21:
        print("Good evening sir...")
        speak("Good evening sir...")
    else:
        print("Good night sir...")
        speak("Good night sir...")


# THIS IS THE DRIVER CODE
if __name__ == '__main__':
    wishme()
    while True:
        query = take_command().lower()
        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            text = "The time is " + strTime
            print(text)
            speak(text)

        elif 'date' in query:
            today = datetime.date.today()
            date = today.strftime("%B %d, %Y")
            text = "The date is " + date
            print(text)
            speak(text)

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            text = "According to Wikipedia" + wikipedia.summary(query, sentences=3)

            print(text)
            speak(text)

        elif 'can you repeat that' in query:
            print(text)
            speak(text)

        elif 'search' in query:
            command = query.replace('search', '')
            webbrowser.open('https://www.google.com/search?q=' + command)

        elif 'open' and 'app' in query:
            if 'whatsapp ' in query:
                os.system("open /Applications/WhatsApp.app")
            elif 'safari' in query:
                os.system("""osascript -e 'tell app "Safari" to open'""")

        elif 'open' and 'website' in query:
            for j in search(query, num_results=1):
                webbrowser.open(j)

        # elif 'close window' in query:
        #     os.close(fb=)

        elif 'terminate' in query:
            print("Thank you for using the program.")
            speak("Thank you for using the program.")
            exit()
