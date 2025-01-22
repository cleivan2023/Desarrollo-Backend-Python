"""  Modularizar código
 Tomar los tres casos de los ejercicios A grupal anterior y re escribirlos como funciones"""

def calcular_raiz_cuadrada():
    """
    Calcula la raíz cuadrada de un número ingresado por el usuario
    sin usar la función sqrt de la biblioteca math.
    """
    numero = float(input("Introduce un número para calcular su raíz cuadrada: "))
    if numero < 0:
        print("No se puede calcular la raíz cuadrada de un número negativo.")
        return
    
    # Usando el método de aproximación de Newton-Raphson
    aproximacion = numero / 2.0
    while True:
        mejor_aproximacion = (aproximacion + numero / aproximacion) / 2.0
        if abs(mejor_aproximacion - aproximacion) < 1e-10:  # Tolerancia
            break
        aproximacion = mejor_aproximacion
    
    print(f"La raíz cuadrada aproximada de {numero} es {mejor_aproximacion}")

# Llamada a la función
calcular_raiz_cuadrada()
 

 ###################################################################################
def calcular_distancia_euclidiana():
    """
    Calcula la distancia euclidiana entre dos puntos dados por el usuario.
    """
    print("Introduce las coordenadas del primer punto:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    
    print("Introduce las coordenadas del segundo punto:")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    
    # Fórmula de distancia euclidiana
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print(f"La distancia euclidiana entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es {distancia:.2f}")

# Llamada a la función
calcular_distancia_euclidiana()

###################################################################################
def invertir_palabra():
    """
    Solicita una palabra al usuario, la invierte y la muestra junto con la original.
    """
    palabra = input("Introduce una palabra: ")
    palabra_invertida = palabra[::-1]
    print(f"Palabra original: {palabra}")
    print(f"Palabra invertida: {palabra_invertida}")

# Llamada a la función
invertir_palabra()

