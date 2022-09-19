"""
Faça um programa que converte um número decimal para binário. Por exemplo
23 10 = 11101 2.
"""

numero = int(input('Digite um número: '))
binario = ''
elemento = -1

while numero != 0:

    if numero % 2 == 1:
        binario += '1'

    if numero % 2 == 0:
        binario += '0'

    numero = numero // 2

for _ in range(len(binario)):
    print(binario[elemento], end='')
    elemento -= 1
