lista_de_numeros = []

for numero in range(10):
    numero = int(input('Digite um número: '))
    lista_de_numeros.append(numero**2)
print(sum(lista_de_numeros))

