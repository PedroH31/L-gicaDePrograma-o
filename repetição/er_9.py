"""
Faça um programa que lê um número inteiro de 1 a 30, caso o número informado
seja maior que 0 e menor que 31, deve ser exibida a mensagem “Numero valido”,
caso contrário, deve ser exibida a mensagem “Tente novamente” e o usuário deve
digitar o número novamente. O programa só termina quando um número válido é
informado.
"""


while True:
    numero = int(input('Digite um número: '))
    if 0 < numero < 31:
        print('Número válido.')
        break
    else:
        print('Tente novamente.')
        