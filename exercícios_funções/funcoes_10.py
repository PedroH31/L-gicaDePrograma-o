"""
Data com mês por extenso.
Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no
formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
"""
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o ano: '))


def mes_por_extenso(mes_extenso):
    meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
             9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

    for chave, valor in meses.items():
        if mes_extenso == chave:
            return valor


mes_escrito = mes_por_extenso(mes)
print(f'({dia}/{mes_escrito}/{ano})')
