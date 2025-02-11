"""  Función distancia como “lambda”
 • Escriba nuevamente la función de distancia euclidiana.
 • Transforme la función a una función anónima (lambda).
 • Su programa debe recibir las coordenadas por la entrada estándar y luego llamar a 
la función anónima.
 • La función anónima debe retornar la distancia euclidiana (presente el resultado 
por la salida estándar)."""

import math

# Función lambda para calcular la distancia euclidiana
#Creamos una función anónima que toma cuatro argumentos: (x1, y1, x2, y2). Aplicamos la fórmula de la distancia euclidiana usando math.sqrt().

distancia = lambda x1, y1, x2, y2: math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Entrada de datos por consola
#Pedimos al usuario que ingrese las coordenadas.
#input() recibe los valores como texto.
#split() los separa en dos valores.
#map(float, ...) convierte los valores en números decimales (float).

x1, y1 = map(float, input("Ingrese x1 y1 separados por espacio: ").split())
x2, y2 = map(float, input("Ingrese x2 y2 separados por espacio: ").split())

# Calcular y mostrar la distancia
#Llamamos a la función lambda con las coordenadas ingresadas.
#Mostramos el resultado con dos decimales (.2f).
resultado = distancia(x1, y1, x2, y2)
print(f"La distancia euclidiana es: {resultado:.2f}")

