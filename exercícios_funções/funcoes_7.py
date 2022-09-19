"""
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
"""


def quantidade_de_digitos(n: int):
    digitos = ''
    digitos += str(n)

    print(f'Quantidade de digitos do número: {len(digitos)}')


numero = int(input('Digite um número: '))

quantidade_de_digitos(numero)
