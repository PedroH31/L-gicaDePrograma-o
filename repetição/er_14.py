lista_de_bois = []

while True:
    peso = float(input('Digite o peso do boi(em kg): '))
    lista_de_bois.append(peso)
    if peso == max(lista_de_bois):
        print(f'O novo maior peso é: {max(lista_de_bois)}kg.')
    elif peso < 0:
        lista_de_bois.remove(-1)
        print(f'O menor peso é: {min(lista_de_bois)}kg.')
        break
