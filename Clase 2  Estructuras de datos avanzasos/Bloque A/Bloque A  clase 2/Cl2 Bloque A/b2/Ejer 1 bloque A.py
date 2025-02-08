"""  1. Cálculo de promedio y rango
 a. Crear una lista con los siguientes números:
 10, 20, 5, 60, 20, 10(enesteorden).
 b. Determine elrango del conjunto de números.
 c. Determine elpromedio haciendo uso del ciclo for.
 d. Determine elpromedio haciendo uso de las funciones genéricas que 
aplican sobre la lista."""

# a. Crear la lista con los números dados
numeros = [10, 20, 5, 60, 20, 10]

# b. Determinar el rango (máximo - mínimo)
rango = max(numeros) - min(numeros)
print(f"Rango: {rango}")  # Imprime el rango calculado

# c. Determinar el promedio usando un ciclo for
suma = 0
for numero in numeros:
    suma += numero  # Se suma cada número de la lista
promedio_for = suma / len(numeros)  # Promedio = suma de los números / cantidad de números
print(f"Promedio (usando ciclo for): {promedio_for}")  # Imprime el promedio calculado con el ciclo for

# d. Determinar el promedio usando las funciones genéricas
promedio_funcion = sum(numeros) / len(numeros)  # sum() calcula la suma de todos los elementos, len() cuenta cuántos elementos hay
print(f"Promedio (usando funciones genéricas): {promedio_funcion}")  # Imprime el promedio calculado con las funciones genéricas

