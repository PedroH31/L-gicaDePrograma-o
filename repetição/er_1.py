"""
Faça um programa que receba repetidamente o ano de nascimento e o sexo (em
formato de caractere) de duas pessoas que formam um casal. Para casais
compostos por pessoas de sexos diferentes, o programa deve exibir na tela o sexo
da pessoa mais nova. Por exemplo, se a primeira pessoa nasceu em 1993, e é do
sexo masculino, e a segunda pessoa nasceu em 1997, e é do sexo feminino, deve
ser exibida a mensagem “A pessoa do sexo feminino e mais nova”. Caso o casal
seja formado por pessoas do mesmo sexo, o programa deve contar a quantidade
de casais, cujas pessoas tenham nascido no mesmo ano, e exibir esta informação
uma única vez ao término do programa. O programa deve repetir este processo
até que pelo menos um dos anos informados seja negativo.
"""
casais = []
mesmo_ano = 0

while True:
    ano = int(input('Digite o ano de nascimento: '))
    sexo = input('Digite o sexo(masculino/feminino): ')
    ano1 = int(input('Digite o ano de nascimento: '))
    sexo1 = input('Digite o sexo(masculino/feminino): ')
    casais.append(ano)
    casais.append(ano1)
    if ano > ano1:
        print(f'A pessoa do sexo {sexo} é mais nova.')

    elif ano1 > ano:
        print(f'A pessoa do sexo {sexo1} é mais nova.')

    elif ano == ano1:
        mesmo_ano += 1

    elif sexo == sexo1:
        print(f'Casais nascidos no mesmo ano: {mesmo_ano}')

    elif 0 > ano or ano1 < 0:
        break

