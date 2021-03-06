import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import operator
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id) #for female voice one can use [1] instead of [0]


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
   
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir")

    elif hour>=12 and hour<18:
        speak("Good afternoon sir")

    
    else:
        speak("good evening sir")

    speak("jarvis here. how can i help you")

def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizng...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        print(e)
        print()
        return "none"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'how are you' in query:
            speak("i am fine,,,, how about you")

        elif 'i am fine' in query:
            speak("ok  then,,,,whats up")

        elif 'nothing' in query:
            speak("nothing special ! today them should i open any entertaining ")
            
        elif 'who is' in query:
            speak('searching on wikipedia sir...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'what is' in query:
            speak('searching on wikipedia sir...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gaana' in query:    #this feature is for opening such sites which play songs you can type here any music playing site. example 'spotify'
            webbrowser.open("gaana.com")
            speak("according to greek philospher DEMOCRITUS, no one can understand ones favourites so please type your favourite song on your own")

        elif 'where is' in query:
            from selenium import webdriver 
from time import sleep 

driver = webdriver.Chrome("/home/arun/Downloads/chromedriver") 
driver.get("https://www.google.co.in/maps/@10.8091781,78.2885026,7z") 
sleep(2) 

def searchplace():
	   Place=driver.find_element_by_class_name("tactile-searchbox-input")
	   Place.send_keys(query)
	   Submit=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
	   Submit.click()
searchplace()

def directions():
	   sleep(10)	
	   directions=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div/button")
	   directions.click()
directions()

def find():
         sleep(6)
         find=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
         find.send_keys("Tirunelveli")
         sleep(2)
         search=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
         search.click()
find()

        elif 'hello' in query:
            speak("hello sir,,,, how can i help you")

        elif 'hey jarvis' in query:
            speak("yes sir,,,,,,, any work to doo?")
       
        elif 'open hotstar' in query:  #one can type any digital platform site to enjoy
            webbrowser.open("www.hotstar.com/in")

        elif 'world blog' in query: #you can type here any blog site you read
            webbrowser.open("paleontologyworld.com")
            speak("hope you will get more paleontological facts")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        ''''
        to start any application use this sketetal code
        elif 'open [your application name]' in query:
            [your application name]Path = 'application path in file manager'
            os.startfile([your application name]Path)
