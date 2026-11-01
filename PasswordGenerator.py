import string
import secrets
import random

def psw_generator(psw):
    strings = ''
    while True:
        try:
            user_input = int(input('How many characters should the password be?: '))
        except ValueError:
            print('Must be a whole number')

psw_generator('asd')
    