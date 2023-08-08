"""Escribir un programa que pida al usuario una palabra y muestre por
pantalla el número de veces que contiene cada vocal."""
vocals = ['a', 'e', 'i', 'o', 'u']
counts = []
word = input("Ingresea una palabra(\'err\' para salir): ")

while word != 'err':

    [print('Cantidad de ' + vocal + '\'s: ', word.count(vocal))
     for vocal in vocals]

    word = input("Ingresea una palabra(\'err\' para salir): ")
