"""
Faça um programa que recebe como entrada um número inteiro e informa se este
número é primo. Um número primo só é divisível por 1 e por ele mesmo

"""
numero = int(input('Digite um número inteiro: '))

if numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(f'{numero} não é um número primo.')
            break
        else:
            print(f'{numero} é um número primo.')
            break


