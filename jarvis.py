import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
# import gtts as gTTS
# for female voice (hindi english both)
from gtts import gTTS
from playsound import playsound

# # for male voice (just english)
# import pyttsx3
# engine = pyttsx3.init('sapi5')
# voices= engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

def speak(audio):

# for male voice (just english)
    # engine.say(audio) 
    # engine.runAndWait()

# for female voice (hindi english both)
    sp = gTTS(audio)
    date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice"+date_string+".mp3"
    sp.save(filename)
    playsound(filename)
    os.remove(filename)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak('Good Morning Deeepak ')
    elif hour >=12 and hour < 18:
        speak('Good afternoon Shivam')
    else:
        speak('Good Evening Shivam')

    speak('I am jarvish sir , how can i help you')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
       print('Recognizing...')
       query = r.recognize_google(audio,language = 'en-in')
       print(f"You said : {query}\n")
    except Exception as e :
        print("Say that again please ")
        speak("Sorry i didn't get it , Say that again please")
        return 'none'
    return query


if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        if 'who is' in query:
            speak('searching wikipedia')
            query =  query.replace('tell me who is', "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(f"according to wikipedia {results} ")
    
        elif 'google' in query:
            speak('opening google sir')
            query = query.replace('search', "")
            query = query.replace('google', "")
            query = query.replace('open', "")
            query = query.replace('and', "")
            query = query.replace('ok jarvis', "")
            webbrowser.open(f'https://www.google.com/search?q={query}')

        elif 'youtube' in query:
           speak('opening youtube sir')
           query = query.replace('search', "")
           query = query.replace('open', "")
           query = query.replace('youtube', "")
           query = query.replace('and', "")
           query = query.replace('in', "")
           query = query.replace('ok jarvis', "")
           webbrowser.open(f'https://www.youtube.com/results?search_query={query}')

        elif 'instagram' in query:
           speak('opening instagram sir')
           webbrowser.open('https://www.instagram.com/')
           if "shashank" in query:
              speak("opening shashank's chat sir")
              webbrowser.open('https://www.instagram.com/direct/t/340282366841710300949128118831534800539')
           elif "shubham" in query:
              speak("opening shubham's chat sir")
              webbrowser.open('https://www.instagram.com/direct/t/340282366841710300949128194443191805386')

        elif 'music' in query:
            speak('playing music sir')
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[2]))
    
        elif "time" in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"Sir the time is  {strTime}")

        elif "john" in query:
           speak("sorry sir but my name is not john , it's jarvish")

        elif "telegram" in query:
           speak('opening telegram sir')
           os.startfile("C:\\Users\\patha\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")

        elif "score" in query:
           speak('wait a moment please')
           speak('here is the score')
           result = webbrowser.open("https://m.cricbuzz.com/live-cricket-scores/")
        elif "chod" in query:
           speak('behen ke lawde gali mat de varna aapki maa chod dungi')
        elif "girlfriend" in query:
           speak('kutiya banegi aapki Girlfriend')
        elif "deepak" in query:
           speak('Sorry deepak sir , good morning deepak')

        elif "square" in query:
           speak(f'the square of 29 is {29*29}')
        elif "cube" in query:
            speak(f'the cube of 58 is {58*58*58}')
        elif "stop" in query:
            break
        elif "bye jarvis" in query:
          speak("bye sir Have a nice day")
          break
        elif "jarvis bye" in query:
          speak("bye sir Have a nice day")
          break
        elif "buy jarvis" in query:
          speak("bye sir Have a nice day")
          break
