"""
Modifique o programar anterior para mostrar a porcentagem dos números
múltiplos de 5 dentre todos os números digitados.
"""

total_de_numeros = []
multiplos_de_5 = 0  # armazena os números que forem multiplos de 5

while True:
    numero = int(input('Digite um número inteiro: '))
    total_de_numeros.append(numero)

    if (numero % 5) == 0:
        multiplos_de_5 += 1

    if numero == 0:
        del total_de_numeros[-1]
        multiplos_de_5 -= 1
        porcentagem_dos_multiplos = (multiplos_de_5 * 100) // len(total_de_numeros)
        print(f'Porcentagem dos números multiplos de 5: {porcentagem_dos_multiplos}%')
        break



