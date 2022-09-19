"""
Faça um programa com uma função chamada somaImposto.
A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem
e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o
imposto sobre vendas.
"""


def soma_imposto(taxaimposto, custo):
    imposto = (taxaimposto * (1/100)) * custo
    valor_com_imposto = custo + imposto
    return valor_com_imposto


print(soma_imposto(16, 100))
