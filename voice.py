#VOICE vala part

import speech_recognition as sr
import datetime

r = sr.Recognizer()

'''
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)'''

def speak(audio):
    import pyttsx3
    engine=pyttsx3.init()

    print("SPEAKING",audio)
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning sir!")
    elif hour < 18:
        speak("Good afternoon sir!")
    else:
        speak("Good evening sir!")
    speak("What can I do for you?")

import speech_recognition as sr

def takeCommand():
    try:
        with sr.Microphone() as source:
            print("Listening...")

            r.dynamic_energy_threshold = True
            r.adjust_for_ambient_noise(source, duration=1)
            r.pause_threshold = 0.6
            r.non_speaking_duration = 0.3

            audio = r.listen(source, timeout=5, phrase_time_limit=4)

        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()

    except sr.WaitTimeoutError:
        # No speech detected → just continue loop
        print("No speech detected")
        return "None"

    except sr.UnknownValueError:
        return "None"

    except Exception as e:
        print("Error:", e)
        return "None"
    
