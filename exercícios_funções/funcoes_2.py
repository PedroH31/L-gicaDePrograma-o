"""
Faça um programa para imprimir:

        1
        1   2
        1   2   3
        .....
        1   2   3   ...  n

    para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""


def escada(numero: int):
    for n in range(1, numero + 1):
        for i in range(1, n + 1):
            print(i, end='   ')
        print('')


escada(10)

