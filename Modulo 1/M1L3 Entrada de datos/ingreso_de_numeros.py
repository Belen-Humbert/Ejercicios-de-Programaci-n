# Para devolver un nuevo número entero a partir de un tipo de datos diferente,
# utiliza la función int().

# Para guardar los datos de entrada en una variable como un número inmediatamente,
# puedes aplicar el método int() directamente a input():

# Pedimos al usuario que introduzca un número y lo convertimos directamente a un entero usando int().
e = int(input("Introduce un número:"))  # Aquí, la entrada del usuario se convierte en un número entero y se guarda en la variable 'e'.

# Pedimos al usuario que introduzca otro número y hacemos lo mismo, almacenándolo como un entero en 'f'.
f = int(input("Introduce un número:"))  # La entrada se convierte y almacena como un número entero en la variable 'f'.

# Después de esta entrada, los valores de las variables se almacenan inmediatamente como un tipo de datos numéricos,
# lo que significa que puedes realizar operaciones matemáticas normales con ellos:

# Sumamos las dos variables numéricas ('e' y 'f') y guardamos el resultado en 'g'.
g = e + f  # La suma de los números ingresados se almacena en la variable 'g'.

# Mostramos el resultado de la suma en la consola.
print(g)  # Aquí imprimimos el valor de 'g', que es la suma de los dos números ingresados.


a = int(input("Introduce el primer número:"))
b = int(input("Introduce el segundo número:"))
e = int(input("introduce un número:"))
f = int(input("introduce un número:"))

g = e + f
print(g)
c = a + b
print(c)

d = int(a) + int(b)
print(d)