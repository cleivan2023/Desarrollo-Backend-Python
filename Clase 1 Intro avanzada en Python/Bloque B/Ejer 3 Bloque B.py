""" ¿Está en el rango?
 • Escriba una función que permita determinar si un número se encuentra en un 
rango determinado.
 • La función debe tener como parámetros el número a testear, el valor inferior del 
rango, el valor superior del rango.
 • La función debe retornar True si el número está en el rango; caso contrario retorna 
False."""

def esta_en_rango(numero, rango_inferior, rango_superior):
     """
    Determina si un número está dentro de un rango dado.
    
    Parámetros:
    - numero (int o float): El número a evaluar.
    - rango_inferior (int o float): El límite inferior del rango.
    - rango_superior (int o float): El límite superior del rango.
    
    Retorna:
    - True si el número está en el rango (incluyendo límites).
    - False en caso contrario.
    """
     
     # Ejemplo de uso:

num = float(input("Introduce el numero a evaluar"))
limite_inferior = float(input("Introduce el limite inferior del rango: "))
limite_superior = float(input("Introduce el limite superior del rango: "))

if esta_en_rango(num, limite_inferior, limite_superior):
    print(f"El numero {num} esta dentro del rango [{limite_inferior}, {limite_superior}].")
else:
    print(f"El numero {num} NO está dentro del rango [{limite_inferior}, {limite_superior}].")


