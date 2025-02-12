"""  Determinar el mayor valor en una lista con reduce()
• Escriba un programa que reciba una lista y permita determinar el valor mayor.
 • Debe usar una operación tipo “reduce()” para realizar las comparaciones.
 • El programa debe imprimir por pantalla el valor mayor de la lista."""

from functools import reduce  # Importamos reduce

# Definir la lista de números, Aquí puedes ingresar cualquier lista de números.
numeros = [12, 45, 23, 89, 34]

# Usar reduce() para encontrar el mayor valor, reduce() recorre la lista comparando de dos en dos
mayor = reduce(lambda x, y: x if x > y else y, numeros)

#Compara 12 y 45, elige 45.
#Compara 45 y 23, elige 45.
#Compara 45 y 89, elige 89.
#Compara 89 y 34, elige 89.
#Resultado final: 89.

# Mostrar el resultado
print(f"El número mayor es: {mayor}") #Un f-string (f"") permite incluir variables dentro de una cadena de texto de manera sencilla y legible.


