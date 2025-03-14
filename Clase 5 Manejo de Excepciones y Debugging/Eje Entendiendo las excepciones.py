"""Entendiendo las excepciones:
 • Investigue posibles excepciones aplicables a las listas y diccionarios.
 • Escriba un código que obligue la emergencia de una excepción y captúrela con los 
bloques try/except. Imprima por pantalla el nombre de la excepción y el mensaje.
 • Tip: para identificar las excepciones que aplican a determinados tipos de datos 
usted siempre debe recurrir a la documentación oficial. """

def manejar_excepciones():
    try:
        # 1. IndexError: Acceder a un índice inexistente en una lista
        lista = [1, 2, 3]
        print(lista[5])  # Índice fuera de rango

    except IndexError as e:
        print(f"Excepción capturada: {type(e).__name__} - {e}")

    try:
        # 2. KeyError: Acceder a una clave inexistente en un diccionario
        diccionario = {"nombre": "Juan", "edad": 30}
        print(diccionario["apellido"])  # Clave no existente

    except KeyError as e:
        print(f"Excepción capturada: {type(e).__name__} - {e}")

    try:
        # 3. TypeError: Usar un tipo de dato no hashable como clave en un diccionario
        diccionario = {[1, 2, 3]: "valor"}  # Listas no pueden ser claves

    except TypeError as e:
        print(f"Excepción capturada: {type(e).__name__} - {e}")

    try:
        # 4. ValueError: Intentar eliminar un valor inexistente en una lista
        lista.remove(10)  # 10 no está en la lista

    except ValueError as e:
        print(f"Excepción capturada: {type(e).__name__} - {e}")

# Llamamos la función para ejecutar el manejo de excepciones
manejar_excepciones()

"""Explicación del código:
IndexError: Se intenta acceder al índice 5 de una lista de solo tres elementos.
KeyError: Se intenta acceder a una clave inexistente en un diccionario.
TypeError: Se intenta usar una lista como clave en un diccionario.
ValueError: Se intenta eliminar un elemento que no está en la lista.
Cada excepción es capturada y se imprime su nombre junto con el mensaje de error.   """