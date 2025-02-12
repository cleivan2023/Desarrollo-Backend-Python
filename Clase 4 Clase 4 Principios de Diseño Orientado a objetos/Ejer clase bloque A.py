# clases y objetos en python

#definir una clase:
class Persona:
    nombre = "Juan Perez" # Atributo de la clase

    def get_nombre(self): 
        return self.nombre # Retorna el nombre
    
# creacion de un objetos (instancia de la clase):
x = Persona() # Se instancia la clase fuera del cuerpo de la clase
print(x.get_nombre())  # Se llama al método de la instancia


# Definir una clase con constructor:
class Persona:
    def __init__(self,nombre): # Constructor con el parámetro 'nombre
        self.nombre = nombre  # Asignación del atributo

    def get_nombre(self):  # Se agrega 'self' al método
        return self.nombre  # Retorna el atributo 'nombre'
    
# creacion de un objeto (instancia de la clase)
x = Persona("Juan Perez") # Se instancia con un nombre
print(x.get_nombre()) # Se imprime el resultado
