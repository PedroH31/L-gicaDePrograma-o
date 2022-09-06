"""
Faça um programa que recebe 3 inteiros, correspondentes a um dia, um mês e um
ano. Seu programa deve verificar se a data informada é válida. Verifique se o ano
é bissexto (divisível por 4 e não divisível por 100, ou divisível por 400). Janeiro
tem 31 dias, Fevereiro tem 28 ou 29, Março tem 31, Abril tem 30, Maio tem 31,
Junho tem 30, Julho 31, Agosto 31, Setembro 30, Outubro 31, Novembro 30 e
Dezembro 31.
"""

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
fevereiro = 28

if ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
    fevereiro = 29
elif ano % 4 == 0 and not ano % 100 == 0:
    print(f'O ano {ano} é bissexto.')
    fevereiro = 29
elif ano % 4 == 0 and ano % 100 == 0:
    print(f'O ano {ano} não é bissexto')

if dia == 0 or mes == 0 or ano == 0:
    print('Data inválida.')

elif mes == 1 and dia > 31:
    print('Data inválida.')

elif mes == 2 and dia > fevereiro:
    print('Data inválida.')

elif mes == 3 and dia > 31:
    print('Data inválida.')

elif mes == 4 and dia > 30:
    print('Data inválida.')

elif mes == 5 and dia > 31:
    print('Data inválida.')

elif mes == 6 and dia > 30:
    print('Data inválida.')

elif mes == 7 and dia > 31:
    print('Data inválida.')

elif mes == 8 and dia > 31:
    print('Data inválida.')

elif mes == 9 and dia > 30:
    print('Data inválida.')

elif mes == 10 and dia > 31:
    print('Data inválida.')

elif mes == 11 and dia > 30:
    print('Data inválida.')

elif mes == 12 and dia > 31:
    print('Data inválida.')

else:
    print('Data válida.')
    