"""
Faça um programa que recebe uma quantia (em reais) referente ao saldo de uma
conta poupança e calcula o rendimento que será recebido em 1 ano, desconsidere
a ocorrência de novos depósitos. O banco paga 4% ao ano caso a conta tenha até
R$ 1000,00. 4,5% ao ano, caso a conta tenha um valor acima de R$ 1000,00 e
menor ou igual a R$ 5000,00. E 5% ao ano, para contas com saldo acima de R$
5000,00.
"""

quantia = float(input('Digite uma quantia(em reais): '))

if quantia <= 1000:
    rendimento = quantia * 1.04 - quantia

elif 1000 < quantia <= 5000:
    rendimento = quantia * 1.045 - quantia

else:
    rendimento = quantia * 1.05 - quantia

print(f'em 1 ano, o rendimento recebido foi {rendimento} R$')
