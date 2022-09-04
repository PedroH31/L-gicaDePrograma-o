"""
Faça um programa que recebe um número inteiro e determina se ele é, ou não,
múltiplo de 6.
"""

numero = int(input('Digite um número: '))

if numero % 6 == 0:
    print(f'O número {numero} é multiplo de 6.')
else:
    print(f'O número {numero} não é multiplo de 6.')
    