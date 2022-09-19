"""
Faça um programa que recebe repetidamente o peso de um boi (em quilogramas).
Seu programa deve verificar se o peso do boi atual é maior que o maior peso
informado, caso seja, deve exibir na tela “O maior peso e: ” seguido do novo
maior peso. O programa deve repetir este processo até que o usuário informe um
peso negativo. Ao término do programa, exiba uma única vez o menor peso
informado. OBS: O menor peso informado não será o peso negativo.
"""

peso = float(input('Digite o peso do boi(em kg): '))
maior_peso = peso
menor_peso = peso

while True:
    peso = float(input('Digite o peso do boi(em kg): '))

    if peso > maior_peso:
        maior_peso = peso
        print(f'O novo maior peso é: {maior_peso}kg.')
    if peso < 0:
        print(f'O menor peso é: {menor_peso}')
        break
    if peso < menor_peso:
        menor_peso = peso



