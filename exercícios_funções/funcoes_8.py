"""
Reverso do número.
Faça uma função que retorne o reverso de um número inteiro informado.
Por exemplo: 127 -> 721.
"""


def reverso_do_numero(n: int):
    inverso = str(n)
    print(inverso[::-1])


numero = int(input('Digite um número: '))

reverso_do_numero(numero)
