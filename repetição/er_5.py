numero = int(input('Digite um número: '))
lista_de_numeros = [int(x) for x in str(numero)]  # separa os dígitos do número escolhido

for n in lista_de_numeros:
    print(sum(lista_de_numeros))
    break
