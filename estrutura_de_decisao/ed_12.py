"""
Faça um programa que calcula o IMC (massa/altura²) de uma pessoa e indica sua
classificação de peso. Caso o IMC seja menor que 18.5, a pessoa se encontra
abaixo do peso. Caso o IMC seja maior ou igual a 18.5 e menor que 25, a pessoa
tem o peso considerado normal. Caso o IMC seja maior ou igual a 25 e menor
que 30, a pessoa se encontra com sobrepeso. Caso o IMC seja maior ou igual a
30, a pessoa é considerada obesa.
"""

altura = float(input('Digite sua altura(em metros): '))
peso = float(input('Digite seu peso(em kg): '))
imc = peso / (altura**2)

if imc < 18.5:
    print('Abaixo do peso.')

elif 18.5 <= imc < 25:
    print('Peso normal.')

elif 25 <= imc < 30:
    print('Sobrepeso.')

else:
    print('Obeso(a)')
