""" Invertir palabras
 • Escriba un programa que solicite al usuario una palabra.
 • Invierta la palabra y guárdela en una nueva variable.
 • Imprima por pantalla la palabra original y luego la palabra invertida. """

# Solicitar una palabra al usuario
palabra = input("Ingrese una palabra: ")

# Invertir la palabra / Usamos el concepto de slicing
palabra_invertida = palabra[::-1]

# Mostrar la palabra original e invertida
print(f"Palabra original: {palabra}")
print(f"Palabra invertida: {palabra_invertida}")
