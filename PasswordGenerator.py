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
    while True:
        try:
            user_amount = int(input('How many passwords do you want?: '))
            break
        except ValueError:
            print('Must be a whole number')
    strings = string.ascii_letters + string.punctuation if symbols else string.ascii_letters
    if numbers:
        strings += string.digits
    return user_length, strings, user_amount

def psw_generator():
    length, strings, amount = psw_init()
    for j in range(amount):
        password = ''
        for i in range(length):
            password += secrets.choice(strings)
        print(f'Your {j + 1}. password is: {password}')

    
    


psw_generator()