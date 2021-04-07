import time
import threading
from gtts import gTTS # google text to speech 
import tkinter as tk
import playsound # to play saved mp3 file 
import os # to save/open files 
import speech_recognition as sr #convert speech to text
from PIL import Image, ImageTk
class GUI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.value = 0
        self.start()
    def start(self):
        self.root = tk.Tk()
        
        # Define String Var in the field
        self.sv = tk.StringVar()
        self.sv.set("0")
        
        # Label display data bind StringVar
        self.label = tk.Label(self.root, textvariable=self.sv)
        self.image1 = Image.open("ball.jpg")
        self.test = ImageTk.PhotoImage(self.image1)

        self.label = tk.Label(image=self.test)
        self.label.image = self.test
        
        self.label.pack()
        # Button displayl
        self.button = tk.Button(self.root, text='សួរសំនួរ', command=self.change_value_callback)
        self.button.pack()
        self.root.mainloop()
    # Callback that executes # change_value in another thread
    def change_value_callback(self):
        th = threading.Thread(target=self.change_value, args=())
        th.start()
    # Change #StringVar to update
    def talk(self):
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
    def change_value(self):
        #for value in range(100):
       # text=self.talk().lower()
        time.sleep(0.05)
        #self.sv.set(text)
      
        
        f = open("user.txt" , "r")
        if f.mode =="r":
            content = f.read()
            self.respond(content)
        # Label string is updated in GUI thread when #StringVar is changed
        # Show the value that would appear on the # label
        #print(value)
    def respond(self,output):
        num=0
        print(output)
        num += 1
        response=gTTS(text=output, lang='en')
        file = str(num)+".mp3"
        response.save(file)
        playsound.playsound(file, True)
        os.remove(file)
if __name__ =='__main__':
    gui = GUI()
    #gui.start()
    