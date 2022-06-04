import pyttsx3
import random
import time

import speech_recognition as sr


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    words = ["apple", "banana", "orange", "grape", "mango"]
    guesses = 3

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    word = random.choice(words)
    print("I'm thinking one of these words:")
    print("apple, banana, orange, grape, mango")
    print("You have 3 guesses")
    time.sleep(3)
    
    for i in range(guesses):
            print('Guess {}. Speak!'.format(i+1))
            query = takeCommand().lower()
            if query == word:
                speak("You got it")
                break
            else:
                speak("Wrong guess")
    speak("I was thinking about "+word)
    print("I was thinking about "+word)
