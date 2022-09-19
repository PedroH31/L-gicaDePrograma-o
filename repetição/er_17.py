"""
Faça um programa que recebe um número inteiro e o exibe invertido. Por
exemplo, se a entrada for o número 1377, a saída deve ser 7731.
"""

numero = input('Digite um número: ')
ultimo = -1

for idx in numero:
    print(numero[ultimo])
    ultimo += -1
