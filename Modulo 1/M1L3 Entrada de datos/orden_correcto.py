# ¡Vamos a poner las cosas en orden aquí!

# Escribe un programa que le pida al usuario que introduzca un número y lo almacene en la variable 'n'.

# A continuación, el programa debe mostrar los números anteriores y posteriores a la consola.

# Ejemplo:

# El número que le sigue al 7 es el 8

# El número que le precede al 7 es el 6


n = int(input("Introduce un número: "))

print("El número que le sigue al " + str(n) + " es el " + str(n + 1))
print("El número que le precede al " + str(n) + " es el " + str(n - 1))