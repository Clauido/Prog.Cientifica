"""Escribir un programa que pregunte al usuario los números ganadores de
la lotería primitiva, los almacene en una lista y los muestre por pantalla
ordenados de menor a mayor"""
count = 0
lista = []
value = int(
    input('Ingrese el valor {0} de la loteria[-1 para salir]:'.format(count)))
while value != -1 and count < 6:
    while value < -1:
        value = int(input(
            'Ingrese el valor {0} de la loteria[-1 para salir](no puede ser negativo):'.format(count)))
    count += 1
    lista.append(value)
    value = int(
        input('Ingrese el valor {0} de la loteria[-1 para salir]:'.format(count)))
lista.sort()
print(lista)
