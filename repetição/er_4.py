"""
Modifique o programa anterior para exibir os primeiros N números primos, onde
N será informado pelo usuário.
"""
numero = int(input('Digite um número inteiro: '))


for i in range(2, numero):
    if (numero % i) == 0:
        print(f'O número {numero} não é primo.')
        break
    elif numero <= 0:
        print('Número inválido.')
    if i > 1:
        for n in range(2, i):
            if (i % n) == 0:
                break
        else:
            print(i, end=' ')

