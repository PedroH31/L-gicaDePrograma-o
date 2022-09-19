"""
Faça um programa que recebe um número inteiro positivo e calcula o fatorial
deste número.
"""

numero = int(input('Digite um número inteiro: '))
numero_escolhido = numero  # Armazena o número digitado
escopo = range(1, numero)
inverso = -1  # seleciona o ultimo número do escopo

for _ in escopo:
    numero *= escopo[inverso]  # multiplica os números do escopo na ordem inversa e armazena na variável número
    inverso += -1

print(f'O fatorial de {numero_escolhido} é {numero}')
