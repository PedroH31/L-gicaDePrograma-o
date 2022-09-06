"""
Faça um programa que recebe como entrada um ano e informa se ele é, ou não,
bissexto. Um ano é bissexto quando ele é múltiplo de 4, mas não é múltiplo de
100, porém, anos múltiplos de 400 são uma exceção.
"""

ano = int(input('Digite o ano: '))

if ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')

elif ano % 4 == 0 and not ano % 100 == 0:
    print(f'O ano {ano} é bissexto.')

elif ano % 4 == 0 and ano % 100 == 0:
    print(f'O ano {ano} não é bissexto')


