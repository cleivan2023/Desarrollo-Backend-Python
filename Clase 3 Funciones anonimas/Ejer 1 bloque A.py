""" valor absoluto
• Escriba una función lambda que reciba un número y retorne su valor absoluto.
 • Recuerde que el valor absoluto realiza lo siguiente: si el número es positivo o cero, 
devuelve el mismo número; si el número es negativo, devuelve el mismo número 
pero como valor positivo.
El valor absoluto se obtiene eliminando el signo negativo, es decir:

Si el número es positivo o 0, se queda igual.
Si el número es negativo, se convierte en positivo."""

# Función lambda para el valor absoluto
valor_absoluto = lambda x: x if x >=0 else -x

# Pruebas con diferentes valores
print(valor_absoluto(5))   # Caso positivo
print(valor_absoluto(-8))  # Caso negativo
print(valor_absoluto(0))   # Caso con cero


"""  Definición de la función lambda
Creamos una función lambda que toma un número x como argumento.
Si x es mayor o igual a 0, devuelve x sin cambios.
Si x es menor que 0, devuelve -x (cambia el signo a positivo).
💡 Ejemplo:
Si x = -8, la función hace -(-8) = 8."""

#de otra fora es ocupar abs(x), que es la función incorporada de Python para calcular el valor absoluto
print((lambda x: abs(x))(-100))

print((lambda x: x if(x>=0) else -x)(-19))


