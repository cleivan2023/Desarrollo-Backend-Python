""" 2. Estudiantes y sus notas
 Desarrolle un programa que permita almacenar y calcular el promedio de notas
 de cinco estudiantes en una escuela. Cada estudiante tiene tres calificaciones
 en unrango de 1 a 7. Elsistema debe solicitar los datos de los estudiantes y sus
 notas al usuario y luego mostrar el promedio de calificaciones de cada
 estudiante.
 a. Crear un programa que solicite el nombre de cada uno de los cinco 
estudiantes. Para cada estudiante, solicite tres notas. 
b. Almacenar los datos de cada estudiante (nombre y lista de notas) en una 
lista de listas. 
c. Calcular el promedio de notas para cada estudiante. Mostrar el nombre de 
cada estudiante junto con su promedio. 
"""

# a. Crear un programa que solicite el nombre de cada uno de los cinco estudiantes y sus tres notas
estudiantes = []

for i in range(5):  # Loop para 5 estudiantes
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")  # Solicitar el nombre del estudiante
    notas = []  # Crear una lista vacía para las notas del estudiante
    for j in range(3):  # Solicitar 3 notas
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))  # Solicitar cada nota
        notas.append(nota)  # Agregar la nota a la lista de notas
    estudiantes.append([nombre, notas])  # Almacenar el nombre y las notas en la lista de estudiantes

# b. Calcular el promedio de cada estudiante y mostrar el nombre y su promedio
for estudiante in estudiantes:
    nombre = estudiante[0]  # El nombre está en la primera posición de la sublista
    notas = estudiante[1]  # Las notas están en la segunda posición de la sublista
    promedio = sum(notas) / len(notas)  # Calcular el promedio de las notas
    print(f"{nombre} tiene un promedio de {promedio:.2f}")  # Mostrar el nombre y su promedio
