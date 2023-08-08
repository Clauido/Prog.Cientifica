import numpy as np
"""Dada una lista de valores, potencialmente con valores repetidos, generar
una sublista ordenada de valores donde se eliminan los valores repetidos.
"""
lista = [4, 5, 5, 3, 2, 3, 4, 5, 3, 23, 4, 5, 5, 55]
print(np.unique(lista))
