"""
Faça um programa que recebe um número inteiro N, e em seguida, armazena as
N matrículas e as N médias finais dos alunos de uma turma. Por fim, seu
programa deve exibir a matrícula do aluno com a maior nota, e a matrícula do
aluno com a menor nota.
"""
numero_de_alunos = int(input('Digite o número de alunos: '))
matricula = input('Digite a matrícula: ')
media = float(input('Digite a média: '))

alunos = []
maior_nota = []
menor_nota = [media, matricula]
for nota in range(numero_de_alunos - 1):
    matricula = input('Digite a matrícula: ')
    media = float(input('Digite a média: '))
    maior = [media, matricula]
    menor = [media, matricula]

    if maior > maior_nota:
        maior_nota = maior
    if menor < menor_nota:
        menor_nota = menor

print(f'Aluno com a maior nota: {maior_nota[-1]}')
print(f'Aluno com a menor nota: {menor_nota[-1]}')
