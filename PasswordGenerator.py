"""
https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
"""

import random
import string


def password_generator(n, hard):
    letters = [i for i in string.ascii_letters]
    numbers = [i for i in string.digits]
    special = [i for i in string.punctuation]
    library = letters + numbers
    if hard:
        library += special
    password = ''.join(random.sample(library, n))
    print('password: ' + password)


choice = str(input("Would you like your password to be hard? Y/N: "))
isHard = False
length = 6
if choice.lower() == 'y':
    isHard = True
    length = 16
password_generator(length, isHard)
