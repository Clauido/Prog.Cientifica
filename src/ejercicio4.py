import numpy as np
"""Dada una lista de valores, generar la sublista de valores que solo aparecen
una vez en la lista"""
lista = [1, 2, 3, 4, 5, 6, 1, 1, 1, 1, 1, 1, 1,
         1, 4, 4, 4, 4, 4, 5, 5, 5, 5, 7, 8, 9, 10]
uniqueones = np.unique(lista)
