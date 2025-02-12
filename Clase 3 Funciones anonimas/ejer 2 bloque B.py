""" Viento registrado en estaciones de monitoreo
• Cree un programa que solicite el nombre de una estación de monitoreo y los vientos registrados 
(nudos) en las últimas 5, 10, y 15 horas.
 • Almacene esta información en la memoria principal usando diccionarios y listas.
 • Su programa debe crear un nuevo diccionario con los vientos registrados en kilómetros por hora.
 • Además, el programa debe mostrar por la salida estándar el nombre de la estación y los vientos 
registrados (convertidos a kilómetros por hora).
 • Debe usar operación map().
 • Tip: los vientos en una zona calmada están entre los 3 y 10 nudos."""

# Factor de conversión: 1 nudo = 1.852 km/h
FACTOR_CONVERSION = 1.852  

# 1️⃣ Solicitar datos al usuario
estacion = input("Ingrese el nombre de la estación de monitoreo: ")
vientos_nudos = {
    "5 horas": float(input("Ingrese el viento registrado en las últimas 5 horas (nudos): ")),
    "10 horas": float(input("Ingrese el viento registrado en las últimas 10 horas (nudos): ")),
    "15 horas": float(input("Ingrese el viento registrado en las últimas 15 horas (nudos): "))
}

#Pedimos el nombre de la estación (estacion).
#Guardamos los vientos en nudos en un diccionario (vientos_nudos) con claves "5 horas", "10 horas", "15 horas".
#Convertimos los valores a float() para permitir decimales.

# 2️⃣ Convertir nudos a km/h usando map()
vientos_kmh = dict(map(lambda x: (x[0], x[1] * FACTOR_CONVERSION), vientos_nudos.items()))

# Aquí usamos map() para convertir cada velocidad:
#x[0] → clave (ej: "5 horas").
#x[1] * 1.852 → valor convertido a km/h.
#dict(...) convierte el resultado de map() en un diccionario nuevo.
#Ejemplo de conversión si el usuario ingresa 6 nudos para "5 horas":
#6 * 1.852 = 11.11 km/h ✅

# 3️⃣ Mostrar resultados
print(f"\n📍 Estación: {estacion}")
print("🌬️ Vientos registrados (km/h):")
for tiempo, velocidad in vientos_kmh.items():
    print(f"   - {tiempo}: {velocidad:.2f} km/h")

#Muestra el nombre de la estación.
#Recorremos el diccionario vientos_kmh e imprimimos cada tiempo con su velocidad en km/h.
#:.2f → Redondea a 2 decimales.