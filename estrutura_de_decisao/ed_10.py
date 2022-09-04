"""
Faça um programa que determina se um número é divisível por 3, por 4 e por 5
ao mesmo tempo.
"""

numero = int(input('Digite um número: '))

if numero % 3 == 0 and numero % 4 == 0 and numero % 5 == 0:
    print(f'{numero} é divisível por 3, 4 e 5.')
else:
    print(f'{numero} não é divisível.')
