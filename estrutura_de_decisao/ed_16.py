"""
Uma pessoa deseja trocar o piso de sua casa, mas ela está com problemas para
calcular quantas peças, de 0.6 m x 0.6 m, são necessárias para a troca. Faça um
programa que recebe 2 números reais que representam as dimensões, em metros,
de um cômodo. Considerando que este cômodo é retangular, seu programa deve
calcular quantas peças serão necessárias para trocar todo o piso deste cômodo.
OBS: Peças cortadas são descartadas.
"""

largura = float(input('Digite a largura(em metros) do cômodo: '))
comprimento = float(input('Digite o comprimento(em metros) do cômodo: '))
area = largura * comprimento
pecas_usadas = area // 3.6  # calcula quantas peças são necessárias para preencher o piso.
print(f'São necessárias {pecas_usadas} peças para trocar todo o piso.')



