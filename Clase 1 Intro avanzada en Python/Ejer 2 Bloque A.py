"""Calcular la distancia euclidiana entre dos puntos
 • Elaborar un código para el cálculo de la distancia euclidiana entre dos puntos.
 • Recuerde que la distancia euclidiana se calcula en base a las coordenadas x e y 
de ambos puntos.
 • Debe solicitar las coordenadas de los puntos por la entrada estándar e imprimir la 
distancia.
 
"""
import math

# Solicitar las coordenadas del primer punto
x1 = float(input("Ingrese la coordenada x del primer punto: "))
y1 = float(input("Ingrese la coordenada y del primer punto: "))

# Solicitar las coordenadas del segundo punto
x2 = float(input("Ingrese la coordenada x del segundo punto: "))
y2 = float(input("Ingrese la coordenada y del segundo punto: "))

# Calcular la distancia euclidiana /Usamos math porque necesitamos la función sqrt (raíz cuadrada), que nos ayuda a calcular la distancia
distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Mostrar el resultado
print(f"La distancia euclidiana entre los puntos es: {distancia}")
