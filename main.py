import secrets
import string
import random
from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.root.mainloop()


characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
password = []

for x in range(8):
    password.append(secrets.choice(characters))

print(''.join(password))

Application()
