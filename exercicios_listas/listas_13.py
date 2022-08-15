
lista_de_temperaturas = []
acima_da_media = []

for media in range(12):
    temperatura = float(input('Digite a média de temperatura desse mês: '))
    lista_de_temperaturas.append(temperatura)
    media_anual = sum(lista_de_temperaturas) // len(lista_de_temperaturas)
    if temperatura > media_anual:
        acima_da_media.append(temperatura)

print(media_anual)
print(f'Temperaturas acima da média: {acima_da_media}')

