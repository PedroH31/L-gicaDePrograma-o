"""
Faça um programa que calcule a seguinte expressão, sendo n a quantidade de x i s
a serem informados pelo usuário.
"""

numero = int(input('Digite um número: '))
somatorio = 0

for n in range(1, numero + 1):
    somatorio += (n ** 2)

print(somatorio)
