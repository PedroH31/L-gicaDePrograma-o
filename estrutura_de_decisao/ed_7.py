"""
Faça um programa que recebe três números e determina o maior deles.
"""
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite outro número: '))

maior_numero = 0

if numero1 > numero2 and numero1 > numero3:
    maior_numero = numero1

elif numero2 > numero1 and numero2 > numero3:
    maior_numero = numero2

else:
    maior_numero = numero3

print(f'O maior número é {maior_numero}')
