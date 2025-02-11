"""  Dígito verificador en un RUT  
Escriba una función lambda que retorne el dígito verificador de un RUT.
 • La lambda debe recibir como parámetro un RUT sin dígito verificador y retornar 
este último.
 • Revise el algoritmo para dígito verificador en: 
https://es.wikipedia.org/wiki/Rol_%C3%9Anico_Tributario (sección “Procedimiento 
para obtener el dígito verificador"""

# Función lambda para calcular el dígito verificador de un RUT
dv_rut = lambda rut: str("0K987654321"[11 - (sum(int(d) * f for d, f in zip(reversed(str(rut)), [2,3,4,5,6,7]*10)) % 11)])

# Entrada del usuario
rut = input("Ingrese el RUT sin dígito verificador: ")

# Calcular y mostrar el dígito verificador
print(f"El dígito verificador del RUT {rut} es: {dv_rut(rut)}")


""" Explicación paso a paso
reversed(str(rut)) → Invierte el RUT para procesarlo desde el último dígito.

zip(..., [2,3,4,5,6,7]*10) → Asigna los factores en orden cíclico.

sum(int(d) * f for d, f in zip(...)) → Calcula la suma ponderada.

(suma % 11) → Aplica módulo 11.

11 - (suma % 11) → Calcula el DV.

"0K987654321"[...] → Mapea los resultados (10 → "K", 11 → "0", los demás quedan igual).

str(...) → Convierte el resultado en un string para impresión.

"""
