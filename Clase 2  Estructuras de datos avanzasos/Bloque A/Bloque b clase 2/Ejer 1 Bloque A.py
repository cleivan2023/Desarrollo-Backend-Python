"""  1. Registro de personas (Lista de diccionarios)
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
 apellido de cadapersona registrada. """

# Lista vacía para almacenar los registros
personas = []

# Bucle para ingresar los datos
while True:
    # Solicitar el nombre
    nombre = input("Ingresa el nombre de la persona (o 'FIN' para terminar): ")

    # Si el nombre es 'FIN', salimos del bucle
    if nombre.upper() == "FIN":
        break

    # Solicitar el apellido
    apellido = input("Ingresa el apellido de la persona: ")

    # Crear un diccionario con el nombre y apellido
    persona = {"nombre": nombre, "apellido": apellido}

    # Agregar el diccionario a la lista de personas
    personas.append(persona)

# Mostrar la lista de personas registradas
print("\nLista de personas registradas:")
for persona in personas:
    print(f"Nombre: {persona['nombre']}, Apellido: {persona['apellido']}")
