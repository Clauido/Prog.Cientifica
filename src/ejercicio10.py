""".Implementar en Python un algoritmo que permita devolver en que
posición se encuentra un carácter en una lista sencilla lineal.
"""
lista = ['a', 'b', 'c', 'd', 'bb', 'ccc', 'ddd', 'eee', 'fff',
         'ggg', 'hhh', 'iii', 'jjj', 'dfd', 'sdfsd', 'sdfsd', 'ccc']

string = 'ccc'

index = [i for i, val in enumerate(lista) if val == string]
if len(index) > 0:
    print('Las posiciones donde se encuentra el caracter son:', index)
else:
    print('No se encuentra el caracter')
