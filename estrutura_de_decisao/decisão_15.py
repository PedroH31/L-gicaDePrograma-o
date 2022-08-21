lado1 = float(input('Digite o lado do triângulo: '))
lado2 = float(input('Digite o lado do triângulo: '))
lado3 = float(input('Digite o lado do triângulo: '))


if lado1 == lado2 == lado3:
    print('O triângulo é equilátero.')

elif lado1 != lado2 != lado3:
    print('O triângulo é escaleno.')

else:
    print('O triângulo é isósceles.')