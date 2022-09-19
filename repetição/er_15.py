"""
 Diz-se que um número inteiro N é um quadrado perfeito se existirem M números
ímpares consecutivos, a partir do número 1, cuja soma seja igual a N. Por
exemplo, 9 é um quadrado perfeito pois 9 = 1 + 3 + 5. Faça um programa que
recebe um número inteiro e exibe na tela “Este numero eh um quadrado
perfeito”, caso o número seja um quadrado perfeito, ou “Este numero nao eh um
quadrado perfeito”, caso contrário.

"""
numero = int(input('Digite um número: '))
total = 0

for n in range(numero):
    if n % 2 == 1:
        total += n

    if numero == 1:
        total += numero

    if total == numero:
        print('Este número é um quadrado perfeito.')
        break

else:
    print('Este número não é um quadrado perfeito')

