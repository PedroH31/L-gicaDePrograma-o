"""
Faça um programa que recebe um número inteiro N, e em seguida recebe N
números inteiros. Seu programa deve ordenar os elementos do vetor em ordem
crescente, e por fim, exibir os elementos do vetor.
"""

numero_de_elementos = int(input('Digite a quantidade de números: '))
lista_ordenada = []

for n in range(numero_de_elementos):
    numero = int(input('Digite um número: '))
    lista_ordenada.append(numero)

print(sorted(lista_ordenada))
