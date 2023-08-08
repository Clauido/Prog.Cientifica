"""Implementar en Python un algoritmo que permita insertar un nuevo
elemento al medio de una lista. Si el largo de la lista es impar, insertar el
elemento una posición más de la mitad. Si la lista tiene 5 elementos,
colocarla el nuevo elemento en la posición 4 (después del nodo 3).
"""


def inser_half(item, lista):
    longitud = len(lista)

    posicion_insercion = longitud // 2 + (longitud % 2)

    lista.insert(posicion_insercion, item)
    return lista


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
newList = inser_half(100, lista)
print(newList)
