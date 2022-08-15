import random

nome = input('Digite um nome: ').upper()


def embaralhar():
    return ''.join(random.sample(nome, len(nome)))


print(embaralhar())
