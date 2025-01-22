"""String, busca el valor"""

nombre = "Talento fututo"
print(nombre[0]) # imprime T



"""Strings con dos variables y concatenado con el operador +. """

palabra_uno = "Talento"
palabra_dos = "Futuro"
print(palabra_uno + " " + palabra_dos) # imprime “Talento Futuro”


"""String con operador Slice, usando los corchetes cuadrados 
indicando el inicio y el final."""

nombre = "Talento Futuro"
print(nombre[0:7]) #imprime "Talento"

"""si queremos invertir un string"""
nombre = "Talento Futuro"
print(nombre[::-1]) # imprime “orutuF otnelaT”

"""Entrada y salidas"""
edad = int(input("Ingrese edad: "))
print("La edad es: ", edad)    # imprime la edad es :xx
 
edad = int(input("Ingrese edad: "))
print("La edad es: " + edad)


