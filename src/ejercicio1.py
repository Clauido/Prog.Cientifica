import numpy as np
"""Escriba un programa en Python que ingrese por consola los siguientes
parámetros: a, b y c. Evalúe estos parámetros en la siguiente fórmula y
muestre sus resultados.
"""
a = int(input('Ingrese el valor de a: '))
while a == 0:
    a = int(input('Ingrese el valor de a (No puede ser 0): '))

b = int(input('Ingrese el valor de b: '))
c = int(input('Ingrese el valor de c: '))

determinant = b**2-4*a*c

if determinant > 0:
    x1 = (-b+np.sqrt(determinant))/(2*a)
    x2 = (-b-np.sqrt(determinant))/(2*a)
    print('x1=', x1, '\nx2=', x2)
elif determinant == 0:
    x1 = -b/(2*a)
    print('x1=', x1, '\n,x2=', x1)
else:
    print('No existe solución')
