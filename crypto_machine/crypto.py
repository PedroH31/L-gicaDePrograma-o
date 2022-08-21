import random, string


def crypto_machine():
    keys = ''
    values = ''.join(random.sample(keys, k=len(keys)))
    dct_e = {}
    dct_d = {}
    message = input('Encript or decript? ')
