"""
Faça um programa que recebe os sexos e os anos de nascimento dos integrantes
de um casal. Caso o casal seja formado por pessoas de sexos diferentes, seu
programa deve informar qual o sexo do membro mais jovem do casal, por
exemplo, para um casal onde uma das pessoas nasceu em 1990 e é do sexo
feminino, e a outra pessoa nasceu em 1980 e é do sexo masculino, deve ser
exibida a mensagem: A pessoa do sexo feminino eh a mais nova. Caso os
integrantes do casal tenham nascido no mesmo ano, exiba a mensagem: Ambos
nasceram no mesmo ano. Caso o casal seja formado por pessoas de mesmo sexo,
exiba a mensagem: O casal é formado por pessoas de mesmo sexo.
"""

sexo1 = input('Digite o sexo(masculino ou feminino): ')
sexo2 = input('Digite o sexo(masculino ou feminino): ')
ano1 = input('Digite o ano de nascimento: ')
ano2 = input('Digite o ano de nascimento: ')
homo = sexo1 == sexo2

if sexo1 == sexo2:
    print('O casal é formado por pessoas do mesmo sexo.')

elif ano1 < ano2:
    print(f'A pessoa do sexo {sexo1} é a mais nova.')

elif ano2 < ano1:
    print(f'A pessoa do sexo {sexo2} é a mais nova.')

if ano1 == ano2:
    print('Ambos nasceram no mesmo ano.')



