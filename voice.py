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
import tkinter as tk
import threading
import time
CHOICE = [
    'DAROTH',
    'HMMM, I WILL FIND OUT.',
    'DAROT',
    'Be kind to your friend!',
    'DAVID',
    'KEY'
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

# class App(object):
class App(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # self.values = ""
        self.root = tk.Tk()
        # Define String Var in the field
        self.sv = tk.StringVar()
        self.sv.set("0")
        
                # Label display data bind StringVar
        self.label = tk.Label(self.root, textvariable=self.sv)
        self.label.pack()
        # Button display
        self.button = tk.Button(self.root, text='push', command=self.start)
        self.button.pack()
        self.root.mainloop()
        # frame = Label(master)
        # frame.pack()
        # image = Image.open("ball.jpg")
        
        # photo = ImageTk.PhotoImage(image)
        # self.answer_text = tkinter.StringVar()
        # self.crystal_ball = tkinter.Label(frame, image = photo)
        # self.answer = tkinter.Label(frame, font=("Helvetical", 16), textvariable = self.answer_text)
        # self.crystal_ball.image = photo
        # self.crystal_ball.pack()
        # self.answer.place(relx = 0.5, rely = 0.4, anchor=tkinter.CENTER)
        # self.quit_button = tkinter.Button(frame, text = "QUIT", command = frame.quit)
        # self.ask_button = tkinter.Button(frame, text = "ASk", command = self.start)
        # self.ask_button.pack(side = tkinter.LEFT)
    def change_value_callback(self):
        th = threading.Thread(target=self.start, args=())
        # th.start()
    def change_value(self,msg):
        # for value in range(100):
        # time.sleep(0.05)
        # Label string is updated in GUI thread when #StringVar is changed
        # self.sv.set(str(value))
        # Show the value that would appear on the # label
        # print(value)
        self.sv.set(msg)
    def get_answer (self):
        self.answer_text.set(random.choice(CHOICE))

    def start (self):
        self.change_value("Hi")

        while(1):
            # root.update()
            respond("Let's make a command Sir!")
            self.change_value("Let's make a command Sir!")
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
                answer = next(res.results).text
                print("tets  "+ answer)
                respond("The answer is " + answer)
                    
            elif 'open google' in text:
                webbrowser.open_new_tab("https://www.google.com")
                respond("Google is open")
                time.sleep(5)
                
            elif 'youtube' in text: 
                driver = webdriver.Chrome(r"Mention your webdriver location") 
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

# root = tkinter.Tk()
# app = App(root)
# root.mainloop()
if __name__ =='__main__':
    gui = App()
  #  gui.start()