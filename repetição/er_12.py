"""
Faça um programa que recebe um número positivo e realiza sucessivas
multiplicações por 3 até que se tenha um valor maior que 10000. Por exemplo, se
for digitado o número 4, a saída deve ser 4, 12, 36, 108, 324, 972, 2916, 8748,
26244.
"""
numero = int(input('Digite um número: '))

while numero <= 10000:
    numero = numero * 3
    print(numero)

