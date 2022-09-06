"""
Faça um programa que recebe três números inteiros e exibe na tela uma
mensagem informando se os números correspondem, ou não, aos lados de um
triângulo. Considere que para formar um triângulo, cada um dos lados deve ser
menor ou igual à soma dos outros dois. Caso os valores formem um triângulo,
informe também se ele é equilátero (três lados iguais), isósceles (dois lados
iguais) ou escaleno (três lados diferentes)
"""

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))

eh_triangulo = False

if num1 <= num2 + num3 and num2 <= num1 + num3 and num3 <= num1 + num2:
    eh_triangulo = True
    print('Os números correspondem aos lados de um triângulo')
if num1 == num2 and num2 == num3 and num1 == num3:
    print('Equilátero.')

elif num1 != num2 and num2 != num3 and num1 != num3:
    print('Escaleno')

else:
    print('Isósceles')
