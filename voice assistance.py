import warnings
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import random
import wikipedia


warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

def talk(audio):
    engine.say(audio)
    engine.runAndWait()



def rec_audio():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = recog.listen(source)

        data = " "

        try:
            data = recog.recognize_google(audio)
            print("you said: " + data)

        except sr.UnknownValueError:
            print("Assistant could not understand the audio")

        except sr.RequestError as ex:
            print("request error from google speech recognition" + ex)

            return data



def response(text):
    print(text)

    tts = gTTS(text=text, lang="en")

    audio = "Audio.mp3"
    tts.save(audio)

    playsound.playsound(audio)

    os.remove(audio)


def call(text):
    action_call = "assistant"

    text = text.lower()

    if action_call in text:
        return True

    return False


def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January"
        "February"
        "March"
        "April"
        "May"
        "June"
        "July"
        "August"
        "September"
        "October"
        "November"
        "December"
    ]

    ordinals = [
        "1st"
        "2nd"
        "3rd"
        "4th"
        "5th"
        "6th"
        "7th"
        "8th"
        "9th"
        "10th"
        "11th"
        "12th"
        "13th"
        "14th"
        "15th"
        "16th"
        "17th"
        "18th"
        "19th"
        "20th"
        "21st"
        "22nd"
        "23rd"
        "24th"
        "25th"
        "26th"
        "27th"
        "28th"
        "29th"
        "30th"
        "31st"
    ]

    return f'Today is {week_now}, {months[month_now -1]} the {ordinals[day_now -1]}.'

def say_hello(text):
    greet = ["hi", "hey", "greetings", "wassup", "hello", "what's good", "hey there"]

    response = ["hi", "hey", "greetings", "wassup", "hello", "what's good", "hey there"]

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + "."

    return ""


def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if 1 + 3 <= len(list_wiki) - 1 and list_wiki[1].lower() == "who" and list_wiki[i + 1].lower()== "is":
            return list_wiki[i + 2] + " " + list_wiki[i + 3]


        while True:

            try:

                text = rec_audio()
                speak = " "

                if call(text):

                    if "date" in text or "day" in text or "month" in text:
                        get_today = today_date()
                        speak = speak + " " + get_today

                    elif "time" in text:
                        now = datetime.datetime.now()
                        meridien = ""
                        if now.hour >= 12:
                            meridien = "p.m"
                            hour = now.hour - 12
                        else:
                            meridien = "a.m"
                            hour = now.hour

                            if now.minute < 10:
                                minute = "0" + str(now.minute)
                            else:
                                minute = str(now.minute)
                                speak = speak + " " + "It is" + str(hour) + ":" + minute + " " + meridien + "."

                    elif "wikipedia" in text or "wikipedia" in text:
                            if "who is" in text:
                                person = wiki_person(text)
                                wiki = wikipedia.summary(person, sentences=2)
                                speak = speak + " " + wiki

                            response(speak)

            except:
                talk("I dont know that")