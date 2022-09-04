"""
 Diz-se que um número inteiro N é um quadrado perfeito se existirem M números
ímpares consecutivos, a partir do número 1, cuja soma seja igual a N. Por
exemplo, 9 é um quadrado perfeito pois 9 = 1 + 3 + 5. Faça um programa que
recebe um número inteiro e exibe na tela “Este numero eh um quadrado
perfeito”, caso o número seja um quadrado perfeito, ou “Este numero nao eh um
quadrado perfeito”, caso contrário.

"""
numero = int(input('Digite um número: '))
total = 1

for n in range(numero):
    total = total * (n + 1)

print(total)
