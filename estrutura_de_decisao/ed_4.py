"""
Faça um programa que recebe um número real, correspondente a uma quantia
monetária expressa em reais (R$). O programa deve expressar este valor
monetário em cédulas e moedas, de forma a minimizar a quantidade de itens
correspondentes ao troco. Exemplo:
"""

quantia_monetaria = float(input('Digite uma quantia em reais: '))

notas_de_100=notas_de_50=notas_de_20=notas_de_10=notas_de_5=notas_de_2=notas_de_1= 0
moedas_de_50=moedas_de_25=moedas_de_10=moedas_de_5= 0

notas_de_100, quantia_monetaria = divmod(quantia_monetaria, 100)

notas_de_50, quantia_monetaria = divmod(quantia_monetaria, 50)

notas_de_20, quantia_monetaria = divmod(quantia_monetaria, 20)

notas_de_10, quantia_monetaria = divmod(quantia_monetaria, 10)

notas_de_5, quantia_monetaria = divmod(quantia_monetaria, 5)

notas_de_2, quantia_monetaria = divmod(quantia_monetaria, 2)

notas_de_1, quantia_monetaria = divmod(quantia_monetaria, 1)

moedas_de_50, quantia_monetaria = divmod(quantia_monetaria, 0.5)

moedas_de_25, quantia_monetaria = divmod(quantia_monetaria, 0.25)

moedas_de_10, quantia_monetaria = divmod(quantia_monetaria, 0.10)

moedas_de_5, quantia_monetaria = divmod(quantia_monetaria, 0.05)


if notas_de_100 > 0:
    print(f'{notas_de_100} nota(s) de 100')

if notas_de_50 > 0:
    print(f'{notas_de_50} nota(s) de 50')

if notas_de_20 > 0:
    print(f'{notas_de_50} nota(s) de 50')

if notas_de_10 > 0:
    print(f'{notas_de_10} nota(s) de 10')

if notas_de_5 > 0:
    print(f'{notas_de_5} nota(s) de 5')

if notas_de_2 > 0:
    print(f'{notas_de_2} nota(s) de 10')

if notas_de_1 > 0:
    print(f'{notas_de_1} nota(s) de 1')

if moedas_de_50 > 0:
    print(f'{moedas_de_50} moeda(s) de 50')

if moedas_de_25 > 0:
    print(f'{moedas_de_25} moeda(s) de 25')

if moedas_de_10 > 0:
    print(f'{moedas_de_10} moeda(s) de 10')

if moedas_de_5 > 0:
    print(f'{moedas_de_5} moeda(s) de 5')
