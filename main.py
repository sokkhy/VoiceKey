from PIL import ImageTk, Image  
import random
import tkinter


CHOICE = [
    'daroth',
    'darot',
    'david',
    'HMMM, I WILL FIND OUT.'
]

class App(object):
    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()
        
        image = Image.open("ball.jpg")
        photo = ImageTk.PhotoImage(image)
         
        self.answer_text = tkinter.StringVar()
        self.crystal_ball = tkinter.Label(frame, image = photo)
        self.answer = tkinter.Label(frame, font=("Helvetical", 16), textvariable = self.answer_text)
        self.crystal_ball.image = photo
        self.crystal_ball.pack()
        self.answer.place(relx = 0.5, rely = 0.4, anchor=tkinter.CENTER)
        self.quit_button = tkinter.Button(frame, text = "QUIT", command = frame.quit)
        self.ask_button = tkinter.Button(frame, text = "ASk", command = self.get_answer)
        self.ask_button.pack(side = tkinter.LEFT)
    def get_answer (self):
        self.answer_text.set(random.choice(CHOICE))

root = tkinter.Tk()
root.mainloop()
root.destroy()
