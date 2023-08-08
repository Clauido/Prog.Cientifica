import numpy as np
"""Implementar en Python un algoritmo que permita eliminar n nodos a
partir de una posición dada (x) en una lista sencilla lineal.
"""

nodos = 5
posicion = 3

lista = np.array([1, 2, 3, 4, 5])
lista = np.delete(lista, slice(posicion, posicion+nodos))
print(lista)
