"""  2. Cursos y notas de una persona
 • Incrementar la funcionalidad del programa anterior permitiendo que ahora cada
 personacuente con cursosinscritos.
 • Es decir, necesitamos que cada persona contenga un diccionario con claves
 correspondientes a cursos y cada clave con una lista con las notas de dicho
 curso.
 • Todos los datos deben ser solicitados por la entrada estándar. Puede considerar
 ingresar un cursopor persona. Cada cursotendrá3 notas.
 • Alfinalizar, el programa debe imprimir el nombre y apellido, seguido del listado de
 cursos y lospromedios obtenidos en cadacurso."""

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

    # Crear un diccionario para la persona
    persona = {"nombre": nombre, "apellido": apellido, "cursos": {}}

    # Bucle para ingresar los cursos y las notas
    while True:
        # Solicitar el curso
        curso = input("Ingresa el nombre del curso (o 'FIN' para terminar los cursos): ")

        # Si el curso es 'FIN', salimos del bucle de cursos
        if curso.upper() == "FIN":
            break

        # Solicitar las 3 notas para el curso
        notas = []
        for i in range(1, 4):
            while True:
                try:
                    # Verificar que la entrada sea un número
                    nota_input = input(f"Ingrese la nota {i} para el curso {curso}: ")
                    nota = float(nota_input)

                    # Validar que la nota esté en el rango correcto
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break  # Si la nota es válida, salimos del bucle
                    else:
                        print("La nota debe estar entre 0 y 10. Intenta de nuevo.")
                except ValueError:
                    # Capturar el error si la entrada no es un número
                    print(f"'{nota_input}' no es un valor válido. Por favor, ingresa un número válido para la nota.")

        # Guardar las notas en el diccionario de cursos
        persona["cursos"][curso] = notas

    # Agregar la persona a la lista
    personas.append(persona)

# Mostrar los registros con los promedios de cada curso
print("\nLista de personas registradas:")
for persona in personas:
    print(f"\n{persona['nombre']} {persona['apellido']}:")
    for curso, notas in persona["cursos"].items():
        promedio = sum(notas) / len(notas)
        print(f"  Curso: {curso}, Promedio: {promedio:.2f}")

