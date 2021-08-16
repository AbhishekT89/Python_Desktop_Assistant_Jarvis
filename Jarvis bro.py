from os import set_inheritable
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib



#used to take voice of inbuilt
engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')


engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hours=int(datetime.datetime.now().hour)
    if hours>4 and hours <12:
        speak('Good Morining')
    elif hours>12 and hours <18:
        speak('Good Afternoon')
    elif hours>18 and hours <22:
        speak('Good Evening')
    else:
        speak('Working Late Sir, By the way')
    speak('I am jarvis Sir. Please tell me how may i help you')

#It take microphone input from user and return string output
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1    #seconds of non-speaking audio before a phrase is considered complete
        audio= r.listen(source)

    try:
        print('Recognizing....')
        query=r.recognize_google(audio ,language='en-in')
        print(f'User said: {query} \n')

    except Exception as e:
        # print(e)

        print("Say That again please...")
        return 'None'
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abhishek891999@gmail.com','Mh04Bc6961')
    server.sendmail('abhishek891999@gmail.com',to,content)



if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching wikipedia.....')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
        
            music_dir=r'C:\Users\abhis\Desktop\Jarvis\song'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'sir, the time is {strTime}')

        elif 'open code' in query:
            codePath="C:\\Users\\abhis\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            print('here')
            try:
                speak('what should i say?')
                content =takeCommand()
                to='aniket6961@gmail.com'
                sendEmail(to,content)
                speak('Email has been sent sir')
            except Exception as e:
                print(e)
                speak('Sorry sir, there is some problem while sending Mail')


        elif 'switch off ' in query:
            speak('Bye, have a nice day sir')
            break

        else:
            speak('Do not no sir, anything else i can help')
        












        #logic  for excuting task based on query

















