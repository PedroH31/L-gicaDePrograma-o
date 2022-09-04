"""
Faça um programa que recebe três números e determina se o terceiro se encontra,
ou não, entre os outros dois.
"""

numero_1 = float(input('Digite um número: '))
numero_2 = float(input('Digite outro número: '))
numero_3 = float(input('Digite outro número: '))

if numero_1 > numero_3 > numero_2:
    print(f'{numero_3} se encontra entre os outros 2 números.')

elif numero_2 > numero_3 > numero_1:
    print(f'{numero_3} se encontra entre os outros 2 números.')

else:
    print(f'{numero_3} não se encontra entre os outros 2 números.')
