tamanho_do_arquivo = float(input('Digite o tamanho do arquivo(em MB) a ser baixado: '))
velocidade_da_internet = float(input('Digite a velocidade da internet(em Mbps): '))
tempo_de_download = (tamanho_do_arquivo / velocidade_da_internet) / 8
print(f'Com uma internet de {velocidade_da_internet} MB levará {tempo_de_download:.2f} minutos para baixar o arquivo.')
