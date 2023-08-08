import numpy as np
import random as rnd
"""Cree un código que genere una lista de 100 números de forma aleatoria
enteros entre 1 y 10.
"""
"""Frecuencia de cada número
Número o números que más se repiten
Número o números que menos se repiten
"""

lista = [rnd.randint(1, 10) for _ in range(100)]

data = np.unique(lista, return_counts=True)

# Frecuencia de cada número
for i in range(len(data[0])):
    print(data[0][i], data[1][i])
print('-'*30)
# Números que más se repiten
[print(data[0][i])
 for i in range(len(data[0])) if data[1][i] == data[1].max()]
# Números que menos se repiten
print('-'*30)
[print(data[0][i])
 for i in range(len(data[0])) if data[1][i] == data[1].min()]
