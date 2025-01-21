""" Cálculo de la raíz cuadrada
 • Elaborar el código para el cálculo de la raíz cuadrada de un número.
 • Restricción: no se puede usar sqrt de la biblioteca de Python.
 • Debe solicitar el número por la entrada estándar e imprimir el resultado.
"""
def raiz_cuadrada_aproximada(numero):
    """
    Calcula la raíz cuadrada de 'numero' usando prueba y error.
    
    Parámetro:
    numero (float): Número del cual se quiere calcular la raíz cuadrada.
    
    Retorna:
    float: La raíz cuadrada aproximada.
    """
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")

    # Comenzamos con 0 y vamos probando números
    aproximacion = 0

    while aproximacion * aproximacion <= numero:
        aproximacion += 0.01  # Incrementamos de a pequeños pasos para mayor precisión

    # Nos pasamos por un poco, entonces retrocedemos
    aproximacion -= 0.01

    return round(aproximacion, 2)  # Redondeamos a 2 decimales

def main():
    try:
        # Solicitar un número al usuario
        entrada = input("Ingresa un número para calcular su raíz cuadrada: ")
        numero = float(entrada)
        
        # Calcular la raíz cuadrada
        resultado = raiz_cuadrada_aproximada(numero)
        
        # Mostrar el resultado
        print(f"La raíz cuadrada aproximada de {numero} es {resultado}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()