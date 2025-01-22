"""  ¿Cuál es el número mayor?
 • Escriba un programa que continuamente pregunte por un número hasta que se 
escriba la palabra “FIN”.
 • En cada ciclo el programa debe actualizar el valor mayor y reportarlo por pantalla.
 • Si no ingresa un valor mayor al anterior, el programa debe continuar mostrando el 
último valor considerado como mayor.
 • ¿Podría reescribir el programa para determinar el número menor?
 • Nota: no se puede usar instrucción de tipo break"""

def determinar_numero_menor():
    """
    Determina el número menor introducido por el usuario hasta que se escriba "FIN".
    """
    menor = None  # Inicialmente, no tenemos ningún número menor.

    while True:
        entrada = input("Introduce un número (o escribe 'FIN' para terminar): ").strip()

        if entrada.lower() == "fin":
            print("Programa terminado.")
            break

        try:
            numero = float(entrada)

            # Comparar el número ingresado con el menor actual
            if menor is None or numero < menor:
                menor = numero
                print(f"Nuevo número menor encontrado: {menor}")
            else:
                print(f"El número menor actual sigue siendo: {menor}")
        except ValueError:
            print("Por favor, introduce un número válido o 'FIN'.")

# Llamar a la función
determinar_numero_menor()

##################################### de otra forma en clases###

FIN = False
mayor = float("-inf")
while not FIN:
    valor = input("ingrese numero: ")

    if valor == "FIN":
        FIN = True
    else:
        if float(valor) > mayor:
            mayor = float(valor)
    print("mayor hasta el momento es:", mayor)