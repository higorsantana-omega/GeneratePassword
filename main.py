import secrets
import string
import random


characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
password = []

for x in range(8):
    password.append(random.choice(characters))

print(''.join(password))
