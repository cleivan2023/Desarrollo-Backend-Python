""" Solucion en clases del ejer 1 """

import geopy
import geopy.distance

class Position:
    def __init__(self, latitude, longitude, altitude):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

class Waypoint(Position):
    def __init__(self, nombre, latitude, longitude, altitude):
        super().__init__(latitude, longitude, altitude)
        self.nombre = nombre

# Creación de los objetos
ciudad1 = Waypoint("Centro", -33, -70, 650)
ciudad2 = Waypoint("CentroSur", -38, -70, 650)

# Cálculo de la distancia
distancia = geopy.distance.geodesic(
    (ciudad1.latitude, ciudad1.longitude),
    (ciudad2.latitude, ciudad2.longitude)
).km

print(f"La distancia entre {ciudad1.nombre} y {ciudad2.nombre} es de {distancia:.2f} km")

