import pyttsx3  # use for speaking # pip3 install pyttsx3
import datetime  # use to get date time
import speech_recognition as sr  # pip3 install speechRecognition
import wikipedia  # pip3 install wikipedia
import webbrowser  # pip3 install webbrowser
import os
import subprocess  # for playing music
import smtplib  # use for sending mail
import sys

engine = pyttsx3.init()


def wishMe():
    '''When Jarvis Starts'''
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak('Good Morning sir')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon sir')
    else:
        speak('Good Evening sir')

    speak('I am Jarvis . How can i help you')


def speak(audio):
    '''It will speak whatever we give input'''
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    '''It takes microphone input from users and returns string output'''

    r = sr.Recognizer()  # it will use to recognize the voices

    with sr.Microphone() as source:
        print('Listing..')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said :- {query}')
    except Exception as e:
        # print(e)
        print('Say that Again Please..')
        return 'None'
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.startfile()
    server.login('youremail@gmail.com', 'yourpassword')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    # speak('Hello , Kaushik Chavda, how are you!')

    if 1:
        wishMe()
        query = takeCommand().lower()
        # query = 'time'

        # Logic for executing tasks on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=1)
            speak('According to wikipedia')
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'play music' in query:
            music_dir = '//home//kaushik//Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            # subprocess.call([music_dir, songs[0]])

        elif 'time' in query:
            strTime = datetime.datetime.now()
            print(strTime)
            speak(f'Sir,the time is ....{strTime}')

        elif 'mail to kaushik' in query:
            try:
                speak('What should i write in e-mail?')
                content = takeCommand()
                to = 'chavdakaushik33@gmail.com'
                sendEmail(to, content)
                speak('E-mail has been send!!')

            except Exception as e:
                print(e)
                speak('Sorry sir , I am not able to send E-mail..')

        elif 'stop' in query:
            sys.exit()
