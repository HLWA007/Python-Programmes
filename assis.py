'''
JARVIS PROGRAMME
This a simple program that acts as a personal assistant. It wishes firsts and asks how can it help? then using microphone listens to query and performs various funtions.
'''
'''
For errors like pip not recognised go to the folder python3.10 in your system
Then copy the path and put the path link to the PATH part of user variables in environment variables
Similarly copy the path of scripts folder too.
Then pip install pyttsx3 in the Windows Powershell.
'''
import pyttsx3 # voice module
import speech_recognition as sr #speech recognizing module
import datetime # date and time format
import wikipedia # for accessing wikipedia
import webbrowser # for opening web browser
import os # for searching or playing music 
import smtplib # for writing mails SMTP protocol

engine = pyttsx3.init('sapi5')
#sapi5 is the voice module of microsoft that is installed in our system by def

voices = engine.getProperty('voices')
#bydef we have 2 types of voices male(david) and female(zira)
#to check the voices write print(voices)
#to check for male voice say print(voices[0].id)
#to check for female voice say print(voices[1].id)
'''
 TTS_MS_EN-US_DAVID_11.0
 TTS -> Text-to-speech
 MS -> MicroSoft
 EN-US -> Engish US
'''


engine.setProperty('voice',voices[1].id)
#using this we have selected the male voice model
#'voice' tells which parameter we want to work on here voice is the parameter

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour<8):
        speak("Good Morning Sir! Namaste! Hope you had a good sleep")
    elif(hour >=8 and hour<12):
        speak("Good Morning Sir! Namaste! Have a great day")
    elif(hour>=12 and hour<19):
        speak("Good Afternoon Sir! Namaste! Hope the day is going Well")
    else:
        speak("Good Night Sir! Its getting late. You should Probably go to bed Sir.")
    
    speak("I am Jarvis. How can i help you?")

def takeCommand():
#   it takes input from microphone and returns output as string
    
    r = sr.Recognizer()
#   its takes input as string

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1 # try more of thesh-holds
        # to check for the meaning of any parameter hold control and click on the program
        # taaki jab bhi mai bolte bolte gap lu ek second ka toh phrase complete na ho jaaye
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        # or u can write print("user said: ", query)
        # here we are recognizing the audio that is being typed

    except Exception as e:
        #print(e) if you want to print the error, donot do it if you are working professionally
        print("say that again please...")
        return "None"    
        #returning None string not python wala None
    return query

def sendEmail(to, content):
    # smtplib pyhton ka package hai jise use krke gmail se emial bhej skte hai 
    # for sending you should allow **less secure apps in gmail for this to work 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.login('chg140100@gmail.com', 'chinu4455')
    server.sendmail('chg140100@gmail.com', to, content)
    server.close()
        
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia......')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open github' in query:
            webbrowser.open("github.com")
        
        elif 'favourite song' in query:
            music_dir = 'C:\\Users\\Dell\\Music\\Songs 2021'
            song = os.listdir(music_dir)
            print(song)
            #use random module to generate a random number so that when ever you play then a random number is generated and random number song is played from the music directory
            os.startfile(os.path.join(music_dir, song[1]))
        
        elif 'motivate' in query:
            music_dir = 'C:\\Users\\Dell\\Music\\Songs 2021\\motivate'
            motivate = os.listdir(music_dir)
            print(motivate)
            #use random module to generate a random number so that when ever you play then a random number is generated and random number song is played from the music directory
            os.startfile(os.path.join(music_dir, motivate[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sure Sir, the time as per the current location is {strTime}")    
            
        elif 'open code' in query:
            codepath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            # You can also keep all your reminders in csv file and use pandas to read csv and numpy to call diff favurs and functions.
            
        elif 'email to' in query:
            try:
                speak('What shuld i say?')
                content = takeCommand()
                to = "aagarwal3_be19@thapar.edu"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry! I was not able to send this email sir.")
