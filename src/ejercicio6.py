import numpy as np
"""Dadas dos listas de valores (sin repeticiones), generar la sublista de
valores que aparecen en ambos.
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [1, 2, 4, 6, 8, 10]
print(np.intersect1d(lista, lista2))
