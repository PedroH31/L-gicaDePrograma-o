"""

Faça um programa para imprimir:

        1
        2   2
        3   3   3
        .....
        n   n   n   n   n   n  ... n

    para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
"""


def escadinha(numero: int):

    for indice in range(1, numero + 1):
        for _ in range(1, indice):
            print(indice, end='   ')
        print('')


escadinha(9)
