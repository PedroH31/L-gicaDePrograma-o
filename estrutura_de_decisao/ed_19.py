"""
Levando em consideração que dia 29/02/2016 é uma segunda-feira, faça um
programa que receba um número inteiro de dias, N. Seu programa deve ser capaz
de informar qual será o dia da semana (domingo, segunda, terça...), N dias após o
dia 29/02/2016.
"""

dia = int(input('Digite o número de dias: '))
semanas = dia // 7


segunda = 7
terca = 1
quarta = 2
quinta = 3
sexta = 4
sabado = 5
domingo = 6


if (semanas * 7) + terca == dia:
    print('terça')

elif (semanas * 7) + quarta == dia:
    print('Quarta')

elif (semanas * 7) + quinta == dia:
    print('Quinta')

elif (semanas * 7) + sexta == dia:
    print('Sexta')

elif (semanas * 7) + sabado == dia:
    print('Sabado')

elif (semanas * 7) + domingo == dia:
    print('Domingo')

else:
    print('Segunda')



