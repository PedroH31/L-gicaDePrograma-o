"""
Faça um programa que recebe vários números inteiros e conta quantos são
múltiplos de 5. O programa deve terminar quando o usuário digitar o número 0.
"""

multiplos_de_5 = 0  # armazena os números que forem multiplos de 5

while True:
    numero = int(input('Digite um número inteiro: '))
    if (numero % 5) == 0:
        multiplos_de_5 += 1

    if numero == 0:
        multiplos_de_5 -= 1
        print(f'Multiplos de 5: {multiplos_de_5}')
        break
