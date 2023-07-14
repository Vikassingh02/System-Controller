import datetime
import webbrowser
import pyttsx3
import os
import smtplib
import speech_recognition as sr

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning.!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Vikku Virus may I help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=2
        audio=r.listen(source)
    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('vsingh08091998@gmail.com','your-password')
    server.sendmail('vsingh08091998@gmail.com',to,content)
    server.close()
if __name__ == "__main__":
    wishMe()
    query=takeCommand().lower()
    if 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open facebook' in query:
        webbrowser.open("facebook.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'open music' in query:
        music_dir='D:\\Videos'
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
    elif 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S") 
        speak(f"sir , the time is {strTime}")
    elif 'open code' in query:
        codePath="C:\\Users\\as\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    elif 'email to vikas' in query:
        try:
            speak("What should I say?")
            content=takeCommand()
            to="vikas.singh2021glbajajgroup.org"
            sendEmail(to,content)    
        except Exception as e:
            print(e)
            speak("sorry my freind vikas singh. I am not able to send this email!")
    
