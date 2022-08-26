"""
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

    F
    FU
    FUL
    FULA
    FULAN
    FULANO
"""

nome = 'FULANO'
escada = []

for letra in nome:
    escada.append(letra)
    print(''.join(escada))


