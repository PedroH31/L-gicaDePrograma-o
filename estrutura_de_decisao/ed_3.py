"""
Faça um programa que identifica se um número inteiro é menor, maior, ou igual
a 20.
"""

numero = int(input('Digite um número: '))

if numero < 20:
    print(f'O número {numero} é menor que 20.')
elif numero > 20:
    print(f'O número {numero} é maior que 20.')
else:
    print(f'O número {numero} é igual a 20.')
    