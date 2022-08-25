import math
"""
Dados dois números, X e Y, onde X deve ser maior que Y, e Y deve ser diferente
de 0, faça um programa que informa o Máximo Divisor Comum entre X e Y.
"""

x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))


if (x > y) and (y != 0):
    while y != 0:
        (x, y) = (y, x % y)
        if y == 0:
            print(f'O MDC entre x e y é: {x}')



