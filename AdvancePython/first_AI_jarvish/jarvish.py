import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#print(voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("I am Jarvis. please tell me how may I help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You said", query)

    except Exception as e:
        #print(e)
        print("say that again please...")
        speak("say that again please...")

        return "none"
    return query
if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open chrome' in query:
            cpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(cpath)
            speak("opening youtube")
        elif 'open google' in query:
                speak("opening google")
                webbrowser.open("google.com")
        elif 'the time' in query:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strtime}")
        elif 'open whatsapp' in query:
                wpath = "C:\\Users\\Mihir\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                speak("Opening Whatsapp")
                os.startfile(wpath)
        elif 'exit' in query:
                speak("good by, have a nice day")
                exit(0)