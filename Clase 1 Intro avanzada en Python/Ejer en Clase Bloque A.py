""" resultado del ejercicio 2 de la distancia """

x1 = int(input("Ingrese la coordenada x del primer punto: "))
y1 = int(input("Ingrese la coordenada y del primer punto: "))
x2 = int(input("Ingrese la coordenada x del segundo punto: "))
y2 = int(input("Ingrese la coordenada y del segundo punto: "))


distancia = ((x2-x1) **2 + (y2-y1) **2) ** (1/2)

print(distancia)