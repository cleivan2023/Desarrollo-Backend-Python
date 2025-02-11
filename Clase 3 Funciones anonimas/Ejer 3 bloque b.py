"""  Viento registrado en estaciones de monitoreo
• Modifique el programa anterior para mostrar por pantalla los vientos que 
sobrepasan los 20 kilómetros por hora.
 • Utilice una operación filter() para complementar el ejercicio anterior de tal manera 
que pueda dar cumplimiento a los requisitos de este ejercicio.

Vamos a modificar el ejercicio anterior para:
✅ Convertir vientos de nudos a km/h con map().
✅ Filtrar los vientos mayores a 20 km/h con filter().
✅ Mostrar solo los vientos que superen 20 km/h."""

from functools import reduce

# Factor de conversión: 1 nudo = 1.852 km/h
FACTOR_CONVERSION = 1.852  

# 1️⃣ Solicitar datos al usuario
estacion = input("Ingrese el nombre de la estación de monitoreo: ")
vientos_nudos = {
    "5 horas": float(input("Ingrese el viento registrado en las últimas 5 horas (nudos): ")),
    "10 horas": float(input("Ingrese el viento registrado en las últimas 10 horas (nudos): ")),
    "15 horas": float(input("Ingrese el viento registrado en las últimas 15 horas (nudos): "))
}

# 2️⃣ Convertir nudos a km/h usando map()
#Convierte cada velocidad multiplicando por 1.852 y lo guarda en un nuevo diccionario.
vientos_kmh = dict(map(lambda x: (x[0], x[1] * FACTOR_CONVERSION), vientos_nudos.items()))

# 3️⃣ Filtrar vientos mayores a 20 km/h usando filter()
# filter() selecciona solo los valores mayores a 20 km/h.
vientos_fuertes = dict(filter(lambda x: x[1] > 20, vientos_kmh.items()))

# 4️⃣ Mostrar resultados
#Imprime todos los vientos convertidos a km/h.
print(f"\n📍 Estación: {estacion}")
print("🌬️ Vientos registrados (km/h):")
for tiempo, velocidad in vientos_kmh.items():
    print(f"   - {tiempo}: {velocidad:.2f} km/h")

# 5️⃣ Mostrar vientos que superan los 20 km/h
#Si hay vientos mayores a 20 km/h, los muestra.
# Si no hay, muestra un mensaje indicando que no hay vientos fuertes.
if vientos_fuertes:
    print("\n⚠️ Vientos fuertes (mayores a 20 km/h):")
    for tiempo, velocidad in vientos_fuertes.items():
        print(f"   - {tiempo}: {velocidad:.2f} km/h")
else:
    print("\n✅ No hay vientos que superen los 20 km/h.")


