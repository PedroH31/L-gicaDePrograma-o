"""
 Um número inteiro positivo N é chamado de número perfeito se ele for igual à
soma de seus divisores positivos diferentes de N. Por exemplo, 6 é um número
perfeito pois 6 = 1 + 2 + 3. 28 é um número perfeito pois 28 = 1 + 2 + 4 + 7 + 14.
8 não é perfeito pois 8 ≠ 1+ 2 + 4. Faça um programa que determina se um
número inteiro positivo é, ou não, um número perfeito.
"""

numero = int(input('Digite um número: '))
divisores = 0

for n in range(1, numero):
    if numero % n == 0:
        divisores += n

    if divisores == numero:
        print('É um número perfeito.')
        break
else:
    print('Não é um número perfeito.')





