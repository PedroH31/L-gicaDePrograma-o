"""
Faça um programa, com uma função que necessite de um argumento.
A função retorna o valor de caractere ‘P’, se seu argumento for positivo,
e ‘N’, se seu argumento for zero ou negativo.
"""


def positivo_ou_negativo(numero):
    if numero >= 0:
        print('Positivo')
    else:
        print('Negativo')


positivo_ou_negativo(100)

