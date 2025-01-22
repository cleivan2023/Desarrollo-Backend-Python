""" ¿Es palíndromo?
 • Escriba un programa reciba como entrada una palabra.
 • Determine si la palabra ingresada es palíndroma.
 • Imprima por pantalla si la palabra es palíndroma.
 Permite ingresar múltiples palabras hasta que el usuario decida salir.
 """

while True:
    palabra = input("Introduce una palabra (o escribe 'salir' para terminar): ").strip().lower()

    # Verifica si el usuario quiere salir
    if palabra =='salir':
        print("Programa terminado. !Hasta luego!")
        break

 # Comprobar si la palabra es un palíndromo

    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        print(f"La palabra '{palabra}' es un palíndromo.")
    else:
        print(f"La palabra '{palabra}' NO es un palíndromo.")

        

