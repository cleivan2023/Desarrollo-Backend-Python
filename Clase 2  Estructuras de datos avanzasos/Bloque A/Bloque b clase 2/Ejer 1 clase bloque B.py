""" EN CLASES: 
1. Registro de personas (Lista de diccionarios)
 Desarrolla un programa que permita registrar el nombrey apellido de varias personas,
 almacenando cada registro en un diccionario y organizando todos los registros en
 una lista.
 a. Solicita al usuario los datos de cada persona. Cada persona debe ser
 almacenada enun diccionariocon las claves "nombre" y "apellido".
 b. Guarda cada diccionario en una lista llamada personas. Cada vez que se
 ingresen los datos de una persona, crea un diccionario y agrégalo a la lista
 personas.
 c. El programa debe continuar solicitando datos hasta que el usuario ingrese "FIN"
 comonombre.
 d. Mostrar la lista de personas. Recorre la lista personas e imprime el nombre y
 apellido de cadapersona registrada."""

final = False
personas = []
while not final:
    nombre = input("ingrese nombre: ")
    if nombre.lower() == 'fin':
        final = True
    else:
        apellido = input("ingrese el apellido: ")
        personas.append({'nombre': nombre, 'apellido': apellido})

    for persona in personas:
        print(persona["nombre"], " ", persona["apellido"])
