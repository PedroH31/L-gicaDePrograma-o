import random

"""
Jogo de Craps. Faça um programa de implemente um jogo de Craps. 
O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
Se, na primeira jogada, você tirar 7 ou 11, você é um "natural" e ganhou. 
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". 
Seu objetivo agora é continuar jogando os dados até tirar este número novamente. 
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
"""
natural = [7, 11]
craps = [2, 3, 12]
lista_de_pontos = []
rodada = 1


def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    resultado = dado1 + dado2

    return resultado


ponto = lancar_dados()
while True:
    jogar = input('Lançar dados?(sim ou não): ')
    lancar_dados()
    lista_de_pontos.append(ponto)
    if jogar == 'sim':
        print(f'Você tirou o número {ponto}!')

    if rodada == 1 and ponto in natural:
        print(f'Você é um natural e ganhou!')
        break
    if rodada == 1 and ponto in craps:
        print(f'CRAPS! Você perdeu.')
        break
    if rodada >= 2 and ponto == 7:
        print('Você perdeu!')
        break
    if rodada >= 2 and ponto in lista_de_pontos:
        print('Você ganhou!')
        break
    rodada += 1
