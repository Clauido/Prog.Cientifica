import numpy as np
"""Ejercicio de transformación de datos:
Dado:
translation_of = {"a": "ade", "c": "cyt","g": "gua", "t": "tym"}
Traducir la lista:
L = ["A", "T", "T", "A", "G", "T", "C"]
En la cadena:
"ade tym tym ade gua tym cyt"
"""
translation_of = {"a": "ade", "c": "cyt", "g": "gua", "t": "tym"}
l = ["A", "T", "T", "A", "G", "T", "C"]
print(translation_of['a'])
[print(translation_of[item.lower()]) for item in l]
