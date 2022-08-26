"""
A sequência de Fibonacci é dada por 1, 1, 2, 3, 5, 8, 13, 21..., ou seja, ela é uma
sequência infinita de números, onde cada termo é formado pela soma dos dois
termos anteriores, com os dois primeiros termos da sequência sendo 1. Faça um
programa que exiba os termos da série que sejam menores que N, onde N será
informado pelo usuário.
"""

numero = int(input('Digite um número: '))
fibonacci = [1, 1]  # armazena a sequência de fibonacci

for _ in range(2, numero):
    ultimo_numero = fibonacci[-1] + fibonacci[-2]  # soma o último número da lista com o penúltimo
    soma_do_ultimo = (fibonacci[-1] + fibonacci[-2])  # soma mais uma vez o último número da lista com o penúltimo
    fibonacci.append(soma_do_ultimo)
    if fibonacci[-1] < numero:
        print(fibonacci)






