"""  Ejemplo: Gestión deInventario deProductos
 Considerando elenunciado anterior, realicemos lo siguiente:
 1.
 Cree un diccionario llamado inventario que representará el inventario
 dela tienda. El inventario deberá contener nombre, cantidad y precio
 detres productos.
 2. Actualizar la cantidad de un producto solicitando los datos al usuario
 (nombre deproducto a actualizar, y cantidad).
 3. Mostrar elinventario completo recorriendo eldiccionario."""

# 1. Crear el diccionario inventario con un producto inicial
inventario = {
    "cod1030": {
        "nombre": "epson 650 vfoto",
        "cantidad": 5,
        "precio": 1000
    }
}

# Mostrar el inventario inicial
print("Inventario inicial:")
for codigo in inventario:
    print(inventario[codigo])

# 2. Actualizar la cantidad de un producto
nombre = "epson 650 vfoto"  # Producto a actualizar
nueva_cantidad = 10  # Nueva cantidad

for codigo in inventario:
    if inventario[codigo]["nombre"] == nombre:
        inventario[codigo]["cantidad"] = nueva_cantidad

# 3. Mostrar el inventario actualizado
print("\nInventario actualizado:")
for codigo in inventario:
    print(f"Código: {codigo}")
    print(f"Nombre: {inventario[codigo]['nombre']}")
    print(f"Cantidad: {inventario[codigo]['cantidad']}")
    print(f"Precio: {inventario[codigo]['precio']}")
    print("-" * 30)

