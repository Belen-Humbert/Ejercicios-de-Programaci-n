# Para asignar un valor de una cadena a una variable, debe especificarse entre comillas:
# 
# nombre = "Nombre"
#
# Vamos a intentar realizar 4 operaciones con cadenas y ver cuáles son posibles:
#
# Cadena + cadena
# La suma de dos cadenas une ambas cadenas en una sola.
# Ejemplo:
# print(nombre + apellido)
#
# Cadena * cadena
# La multiplicación de una cadena por otra no es válida, ya que no se puede repetir una cadena multiplicándola por otra cadena.
# Ejemplo:
# print(nombre * apellido) # Esto dará un error.
#
# Cadena + número
# La suma de una cadena con un número también no es válida sin convertir el número en cadena primero.
# Ejemplo:
# print(nombre + b) # Esto dará un error si b no es una cadena.
#
# Cadena * número
# La multiplicación de una cadena por un número es válida y repite la cadena el número de veces especificado.
# Ejemplo:
# print(nombre * b) # Esto repetirá 'nombre' b veces si b es un número entero.
#
# Podemos sumar cadenas para obtener una única cadena, y también podemos multiplicar una cadena 
# por un número para generar la cadena varias veces.

nombre = "Nombre"
apellido = "Apellido"
b = 5
print(nombre * b)
print(nombre + apellido)
