"""
Duas cidades, A e B, tem populações de 7000 e 20000 habitantes,
respectivamente. A cidade A tem um crescimento populacional de 3,5% ao ano,
enquanto a população da cidade B cresce 1% ao ano. Faça um programa que
calcula a quantidade de anos necessária para que a população da cidade A seja
maior ou igual que a população da cidade B

"""

populacao_a = 7000
populacao_b = 20000
crescimento_a = 1.035
crescimento_b = 1.01
ano = 0

while populacao_a < populacao_b:
    populacao_a = int(populacao_a * crescimento_a)
    populacao_b = int(populacao_b * crescimento_b)
    ano += 1
    print(f'ANOS PASSADOS: {ano}')
    print(f'População A: {populacao_a}')
    print(f'População B: {populacao_b}')

