"""
Faça um programa que recebe um valor inteiro e determina se ele é divisível por
3, se é divisível por 4 e se é divisível por 5. Caso o número não seja divisível por
nenhum dos três, deve ser exibida a mensagem “Nao divisivel”, caso contrário,
informe quais, entre 3, 4 e 5, são seus divisores.
"""

numero = int(input('Digite um número: '))

if numero % 3 == 0:
    print(f'{numero} é divisível por 3.')

if numero % 4 == 0:
    print(f'{numero} é divisível por 4.')

if numero % 5 == 0:
    print(f'{numero} é divisível por 5.')

else:
    print(f'Não divisível.')
