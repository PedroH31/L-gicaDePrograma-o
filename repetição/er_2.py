"""

Faça um programa que mostra uma tabela com as seguintes contagens:
a. De 1 a 100
b. De 10 a 1000 (de dez em dez)
c. De 6 a 204 (apenas os pares)
d. De -1 a -199 (apenas os ímpares)
e. De 100 a 1 (em ordem decrescente)
"""


a = list(range(1, 100))
b = list(range(10, 1010, 10))
c = list(range(6, 204, 2))
d = list(range(-1, -199, -2))
e = list(range(100, 1, -1))

tabela = '\n'.join('{}  {}  {}  {}  {}'.format(f, g, h, i, j) for f, g, h, i, j in zip(a, b, c, d, e))

print(tabela)

