"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo
atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
O programa deve ser encerrado quando não for informado o nome do atleta.
"""

lista_de_saltos = []
nome = input('Digite o nome do atleta: ')
lista_de_saltos.append(nome)


while True:
    lista_de_saltos.append(float(input('Digite a distância do salto: ')))

    if lista_de_saltos == 6:
        print()




