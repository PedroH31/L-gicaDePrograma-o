import math
"""
Faça um programa que recebe um número real com duas casas decimais, assuma
que o usuário irá digitar neste formato, e o arredonda. Caso os dois números da
parte fracionária sejam menores ou iguais a 5, arredonde para baixo, caso
contrário, arredonde para cima.
"""

numero = float(input('Digite um número: '))
parte_fracionaria = numero % 1

if parte_fracionaria <= 0.55:
    print(math.floor(numero))

else:
    print(math.ceil(numero))
    