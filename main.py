import secrets
import string
import random

class Application(): 
    # sequence
    @staticmethod
    def sequence(conditions):
        possible_characters = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
        sequence = ''
        for x in range(len(conditions)):
            if conditions[x]:
                sequence += possible_characters[x]
            else:
                pass
        return sequence

    @staticmethod
    def p_password(sequence, passlength=8):
        password = ''.join(secrets.choice(sequence) for i in range(passlength))
        return password

Application()


    # password