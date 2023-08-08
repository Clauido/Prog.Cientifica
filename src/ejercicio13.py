""".Escribir un programa que almacene el abecedario en una lista, elimine de
la lista las letras que ocupen posiciones múltiplos de 3, y muestre por
pantalla la lista resultante."""

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


filter_abc = [abc[i] for i in range(1, len(abc)) if i % 3 != 0]
print(filter_abc)
