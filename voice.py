import speech_recognition as sr #convert speech to text
import datetime #for fetching date and time
import wikipedia
import webbrowser
import requests
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations
from PIL import ImageTk, Image  
import random
import tkinter
import threading
import time
CHOICE = [
    'DAROTH',
    'HMMM, I WILL FIND OUT.',
    'DAROT',
    'Be kind to your friend!',
    'DAVID',
    'KEY',
]

def talk():
    input=sr.Recognizer()
    with sr.Microphone() as source:
        audio=input.listen(source)
        data=""
        try:
            data=input.recognize_google(audio)
            print("Question :  " + data)
            
        except sr.UnknownValueError:
            print("Sorry I did not hear your question, Please repeat again.")
    return data


def respond(output):
    num=0
    print(output)
    num += 1
    response=gTTS(text=output, lang='en')
    file = str(num)+".mp3"
    response.save(file)
    playsound.playsound(file, True)
    os.remove(file)
    def __init__(self, master,root):
        self.root = root
        frame = tkinter.Frame(master)
        frame.pack()
        image = Image.open("ball.jpg")
        photo = ImageTk.PhotoImage(image)
    def get_answer (self):
        self.answer_text.set(random.choice(CHOICE))

if __name__=='__main__':

    respond("Hi, I am Pike. I will assist you Sir!")
        
    while(1):

        respond("Let's make a command Sir!")
        text=talk().lower()
        if text==0:
            continue
        if "who" in str(text):
            respond(random.choice(CHOICE))
        if "stop" in str(text) or "exit" in str(text) or "bye" in str(text):
            respond("Ok bye and take care")
            break
            
        if 'wikipedia' in text:
            respond('Searching Wikipedia')
            text =text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=3)
            respond("According to Wikipedia")
            print(results)
            respond(results)
                  
        elif 'time' in text:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            respond(f"the time is {strTime}")     
        elif 'search'  in text:
            text = text.replace("search", "")
            webbrowser.open_new_tab(text)
            time.sleep(5)
        
        elif "calculate" or "what is" in text: 
            question=talk()
            print("testss " + text)
            app_id= "H547RP-7YTRPJ77UA"
            client = wolframalpha.Client(app_id)
            res = client.query(text)
            print("result " , res)
            answer = next(res.results).text
            print("tets  "+ answer)
            respond("The answer is " + answer)
            
        elif 'open google' in text:
            webbrowser.open_new_tab("https://www.google.com")
            respond("Google is open")
            time.sleep(5)
            
        elif 'youtube' in text: 
            driver = webdriver.Chrome("D:/Project/python/webpy/VoiceKey/chromedriver.exe") 
            driver.implicitly_wait(1) 
            driver.maximize_window()
            respond("Opening in youtube") 
            indx = text.split().index('youtube') 
            query = text.split()[indx + 1:] 
            driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))              
                
        elif "open word" in text: 
            respond("Opening Microsoft Word") 
            os.startfile('Mention location of Word in your system') 
        
        else:
           respond("Application not available")