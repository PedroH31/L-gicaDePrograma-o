import math

"""
Se um projétil é disparado com uma velocidade inicial V (em m/s) a um ângulo
de inclinação θ (0 < θ < 90), sua posição no plano vertical (x,y) no tempo t
(segundos) é calculada pelas fórmulas que seguem:
x = V * cos(θ) * t
y = V * cos(θ) * t – (g * t²)/2
Considere que g = 9,8 (aceleração da gravidade na Terra)
Faça um programa que, dadas as entradas V e θ, exiba na tela as coordenadas x,y
do projétil, até que o projétil atinja o solo.
"""

v = float(input('Digite a velocidade inicial(em m/s): '))  # velocidade inicial
angulo = float(input('Digite o ângulo de inclinação: '))
gravidade = 9.8
tempo = 0.1
cosseno = math.cos(math.radians(angulo))

x = v * cosseno * tempo
y = v * cosseno * tempo - (gravidade * tempo**2) / 2

if 0 < angulo < 90:
    while y > 0:
        print(x, y)
        tempo += 0.1
        x = v * cosseno * tempo
        y = v * cosseno * tempo - (gravidade * tempo ** 2) / 2

