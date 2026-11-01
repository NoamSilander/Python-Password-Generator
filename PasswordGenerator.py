import string
import secrets
import random

def psw_init():
    while True:
        try:
            user_length = int(input('How many characters should the password be?: '))
            break
        except ValueError:
            print('Must be a whole number')
    while True:
        user_symbol = input('Include symbols (y/n): ').lower()
        if user_symbol == 'y':
            symbols = True
            break
        elif user_symbol == 'n':
            symbols = False
            break
    while True:
        user_symbol = input('Include numbers (y/n): ').lower()
        if user_symbol == 'y':
            numbers = True
            break
        elif user_symbol == 'n':
            numbers = False
            break
    strings = string.ascii_letters + string.punctuation if symbols else string.ascii_letters
    if numbers:
        strings += string.digits
    return user_length, strings

def psw_generator():
    length, strings = psw_init()
    password = ''
    for i in range(length):
        password += secrets.choice(strings)
    print(password)

    
    


psw_generator()