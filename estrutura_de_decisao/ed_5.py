"""
Faça um programa que recebe o consumo de água de uma residência (em metros
cúbicos) e calcula o valor da conta. Considere que o preço do metro cúbico de
água custa R$ 8,50 caso o consumo seja menor que 20 m³, e custa R$ 11,00 caso
o consumo seja maior ou igual a 20 m³
"""

consumo = float(input('Informe a quantidade de água consumida(em m³): '))
menos_de_20 = consumo * 8.50  # calcula o valor da conta caso o consumo seja abaixo de 20m³
mais_de_20 = consumo * 11  # calcula o valor da conta caso o consumo seja maior ou igual a 20m³
if consumo < 20:
    print(f'O valor da conta é de {menos_de_20}')

else:
    print(f'O valor da conta é de {mais_de_20}')
