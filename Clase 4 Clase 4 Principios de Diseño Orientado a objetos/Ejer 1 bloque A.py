""" Creación de objetos complejos
• Cree las clases Waypoint y Trackpoint.
 • La clase Waypoint contiene un nombre; la clase Trackpoint contiene una fecha de 
registro.
 • Ambas clases son posiciones geográficas de tipo Position.
 • La clase Position requiere en su inicialización una latitud, una longitud y una altitud. """

# Clase Position: Representa una posición geográfica con latitud, longitud y altitud.
class Position:
    def __init__(self, latitud, longitud, altitud):
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud

# Clase Waypoint: Hereda de Position y agrega un nombre.
class Waypoint(Position):
    def __init__(self, latitud, longitud, altitud, nombre):
        super().__init__(latitud, longitud, altitud)  # Llama al constructor de Position
        self.nombre = nombre  # Agrega el atributo nombre

# Clase Trackpoint: Hereda de Position y agrega una fecha de registro.
class Trackpoint(Position):
    def __init__(self, latitud, longitud, altitud, fecha_registro):
        super().__init__(latitud, longitud, altitud)  # Llama al constructor de Position
        self.fecha_registro = fecha_registro  # Agrega el atributo fecha de registro

# Ejemplo de uso:
waypoint1 = Waypoint(40.7128, -74.0060, 10, "Nueva York")  # Un punto de referencia
trackpoint1 = Trackpoint(34.0522, -118.2437, 15, "2025-02-12")  # Un punto con fecha

# Mostrar información de los objetos creados
print(f"Waypoint: {waypoint1.nombre}, Ubicación: ({waypoint1.latitud}, {waypoint1.longitud}, {waypoint1.altitud})")
print(f"Trackpoint registrado el {trackpoint1.fecha_registro}, Ubicación: ({trackpoint1.latitud}, {trackpoint1.longitud}, {trackpoint1.altitud})")
