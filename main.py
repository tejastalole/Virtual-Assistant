import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
from datetime import datetime
import time
import subprocess
import random

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except Exception as e:
            print(f"Error: {e}")
            return "Some Error Occurred. Sorry From Siri"

def execute_command(command):
    if open_website(command) or search_google(command) or search_youtube(command) or set_alarm(command) or tell_joke(command) or get_weather(command) or open_application(command):
        return
    if "open settings" in command:
        open_settings()
        return
    if "close settings" in command:
        close_settings()
        return
    if "open letter to principal" in command:
        open_letter_to_principal()
        return
    if "open music" in command:
        musicPath = r"C:\Users\Tejas Talole\Downloads\Night_Drive_Mashup.mp3"
        speak("Opening music...")
        os.startfile(musicPath)
        return
    if "the time" in command:
        current_time = datetime.now().strftime("%H:%M")
        speak(f"Sir, the time is {current_time}")
        return
    if "open vs code" in command:
        vs_code_path = r"C:\Users\Tejas Talole\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        speak("Opening Visual Studio Code...")
        os.startfile(vs_code_path)
        return

def open_website(query):
    sites = {"youtube": "https://www.youtube.com", "wikipedia": "https://www.wikipedia.com", "google": "https://www.google.com"}
    for site in sites:
        if f"open {site}" in query:
            speak(f"Opening {site}...")
            webbrowser.open(sites[site])
            return True
    return False

def search_google(query):
    if "search" in query and "on google" in query:
        search_query = query.replace("search", "").replace("on google", "").strip()
        url = f"https://www.google.com/search?q={search_query}"
        speak(f"Searching for {search_query} on Google")
        webbrowser.open(url)
        return True
    return False

def search_youtube(query):
    if "search" in query and "on youtube" in query:
        search_query = query.replace("search", "").replace("on youtube", "").strip()
        url = f"https://www.youtube.com/results?search_query={search_query}"
        speak(f"Searching for {search_query} on YouTube")
        webbrowser.open(url)
        return True
    elif "play" in query and "on youtube" in query:
        song = query.replace("play", "").replace("on youtube", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)
        return True
    return False

def set_alarm(query):
    if "set alarm for" in query:
        time_str = query.replace("set alarm for", "").strip()
        try:
            alarm_time = datetime.strptime(time_str, "%H:%M").time()
            speak(f"Setting alarm for {alarm_time}")
            while True:
                now = datetime.now().time()
                if now.hour == alarm_time.hour and now.minute == alarm_time.minute:
                    speak("Time to wake up!")
                    break
                time.sleep(30)
        except ValueError:
            speak("Invalid time format. Please use HH:MM format.")
        return True
    return False

def open_settings():
    speak("Opening settings...")
    os.system("start ms-settings:")
    return True

def close_settings():
    speak("Closing settings...")
    os.system("taskkill /F /IM SystemSettings.exe")
    return True

def open_letter_to_principal():
    speak("Opening letter to principal template...")
    letter_content = """Subject: Request for Leave

Respected Principal,

I hope this letter finds you well. I am writing to formally request leave for [mention reason] from [start date] to [end date]. I will ensure to complete all my pending work before my leave and will catch up on any missed lessons.

Thank you for your time and consideration.

Sincerely,
[Your Name]
[Your Class/Designation]"""
    with open("letter_to_principal.txt", "w") as file:
        file.write(letter_content)
    os.system("notepad letter_to_principal.txt")
    return True

def tell_joke(query):
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don’t skeletons fight each other? They don’t have the guts."
    ]
    joke = random.choice(jokes)
    speak(joke)
    return True

def get_weather(query):
    speak("Currently, I am unable to fetch live weather updates, but you can check it on your preferred weather website.")
    return True

def open_application(query):
    if "open calculator" in query:
        speak("Opening Calculator")
        subprocess.run("calc.exe")
        return True
    if "open notepad" in query:
        speak("Opening Notepad")
        subprocess.run("notepad.exe")
        return True
    return False

if __name__ == '__main__':
    speak("Hello Tejas, I am your Virtual Assistant, How Can I Help You")
    while True:
        command = takeCommand()
        execute_command(command)
