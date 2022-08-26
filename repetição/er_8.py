"""
Faça um programa que recebe e calcula o quadrado de vários números. O
programa deve terminar quando o usuário digitar o número 0.
"""

while True:
    numero = int(input('Digite um número: '))
    quadrado = numero**2
    print(quadrado)
    if numero == 0:
        print(f'O número {numero} não tem quadrado.')
        break
