import secrets
import string
import random
from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.labels()
        self.root.mainloop()

    def labels(self):
        self.password_entry = Entry(self.root, width=30)
        self.password_entry.pack()
        
        self.password_lb = Button(self.root, text='Gen')
        self.password_lb.pack()

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
password = []

for x in range(8):
    password.append(secrets.choice(characters))

print(''.join(password))

Application()
