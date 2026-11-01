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
    return user_length, symbols

def psw_generator(psw):
    length, use_symbols = psw_init()
    


psw_generator('asd')