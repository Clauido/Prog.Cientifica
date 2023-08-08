"""Dado un número n, imprima todas las posibles formas de obtenerlo como
productos de dos enteros. Presta atención a las repeticiones
conmutativas. (por ejemplo, 4x9 y 9x4). No incluya repeticiones
conmutativas.
"""
inp = int(input(
    "Ingrese un número para encontrar sus formas de producto[solo Valores positivos](-1 para salir): "))
while int != -1:

    formas = [(i, inp // i) for i in range(1, int(inp**0.5) + 1)
              if inp % i == 0 and i <= inp // i]

    print(formas)
    inp = int(input(
        "Ingrese un número para encontrar sus formas de producto[solo Valores positivos](-1 para salir): "))
