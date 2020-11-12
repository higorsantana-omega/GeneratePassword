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
        self.password_entry.grid(row=0, column=0)
        
        self.password_lb = Button(self.root, text='Gen', command=self.gen_password)
        self.password_lb.grid(row=0, column=1)

    def gen_password(self):
        self.characters = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
        self.sequence=
        self.password = ''

        for x in range(8):
            self.password.join(secrets.choice(self.characters))
            return self.password

        self.password_entry.delete(0, END)
        print(self.password)
        self.password_entry.insert(0, self.password)

Application()
