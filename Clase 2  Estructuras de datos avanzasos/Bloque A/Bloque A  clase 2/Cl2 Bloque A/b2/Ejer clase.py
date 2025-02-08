"""Ejemplo: Gestión de Inventario de Productos
 Considera un sistema de inventario simple para una tienda. Los
 productos están organizados en una lista, y el sistema debe ser capaz de
 realizar varias operaciones para gestionar elinventario.

 1.Cree una lista inicial de productos fija.
 2. Solicita al usuario que agregue tres nuevos productos.
 3. Elimina unproducto específico.
 4. Ordena la lista enorden alfabético.
 5. Muestraelprimer y último producto enorden alfabético. """

#1
productos = ["laptop", "monitor", "mouse"] 

#2
i = 0
while i < 3:
    producto_nuevo = input("ingrese nuevo producto: ")
    productos.append(producto_nuevo) #con el append se agrega los nuevos productos
    i += 1 

print(productos) # zapatillas pantalon cinturon

#3
productos.remove("laptop") # se elimina el primer elemento

print(productos)

#4
productos.sort()

print(productos)

#5
print(productos[0], " ", productos[-1])
print(productos[0], " ", productos[len(productos)-1])

