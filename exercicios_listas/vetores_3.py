"""
Faça um programa que intercala, num terceiro vetor, os elementos de dois
vetores, e por fim, exibe o seu conteúdo. O usuário deve informar o tamanho, e
os elementos, de cada um dos dois vetores. Por exemplo, se o primeiro vetor for
{1, 2} e o segundo vetor for {3, 4}, a saída deve ser {1, 3, 2, 4}.
"""

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
lista3 = lista1 + lista2

print(f'Tamanho: {len(lista3)}, elementos: {lista3}')
