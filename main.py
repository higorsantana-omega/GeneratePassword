import secrets
import string
import random
from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.window()
        self.frame()
        self.labels()
        self.root.mainloop()

    def window(self):
        self.root.geometry('300x300')
        self.root.title('Password Generator')

    def frame(self):
        self.password_fr = Frame(self.root, width=300, height=150, bg='blue')
        self.password_fr.grid(row=0, column=0)

        self.password_bt = Frame(self.root, width=300, height=150, bg='red')
        self.password_bt.grid(row=1, column=0)

    def labels(self):
        self.password_entry = Entry(self.root, width=30)
        self.password_entry.grid(row=0, column=0)
        
        self.password_lb = Button(self.root, text='Gen')
        self.password_lb.grid(row=1, column=0)


characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
password = []

for x in range(8):
    password.append(secrets.choice(characters))

print(''.join(password))

Application()
