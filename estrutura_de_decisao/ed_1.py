"""
Faça um programa que recebe um número real e calcula o quadrado do número,
caso ele seja negativo, ou sua raiz quadrada, caso contrário
"""

numero = int(input('Digite um número: '))
quadrado = numero ** 2
raiz_quadrada = numero**0.5

if numero < 0:
    print(f'O quadrado do número é: {quadrado}')

else:
    print(raiz_quadrada)
