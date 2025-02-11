""" Usa las funciones map(), filter(), y reduce() de functools, que son funciones de
 orden superior que aplican operaciones a listas."""

from functools import reduce # Importamos reduce

lista_original = [2,4,5]
print(lista_original)

# 1️⃣ Elevar al cuadrado cada elemento de la lista
lista_cuadrados = list(map(lambda x: x**2, lista_original))
print(lista_cuadrados)

# 2️⃣ Filtrar los números mayores a 16
lista_filtrada = list(filter(lambda x: x > 16, lista_cuadrados))
print(lista_filtrada)

# 3️⃣ Multiplicar todos los elementos de la lista original
mult = reduce(lambda x, y : x*y, lista_original)
print(mult)

