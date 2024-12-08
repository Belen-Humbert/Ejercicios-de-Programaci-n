# ¡Intentemos implementar nuestro registro en el programa!

# En concreto, mostrando un mensaje sobre el registro exitoso.

# Pedimos al usuario que ingrese su nombre y lo guardamos en la variable "nombre".
nombre = input("Por favor, ingresa tu nombre: ")

# Pedimos al usuario que ingrese sus apellidos y los guardamos en la variable "apellido".
apellido = input("Por favor, ingresa tus apellidos: ")

# Enviamos un mensaje a la consola utilizando las variables "nombre" y "apellido".
print(f"¡Hola {nombre} {apellido}!")
print("Tu registro fue completado con éxito. 😎")

# Ahora refinaremos el registro pidiendo también el e-mail del usuario.

# Pedimos al usuario que ingrese su e-mail y lo guardamos en la variable "email".
email = input("Por favor, ingresa tu e-mail: ")

# Enviamos un mensaje más detallado a la consola incluyendo el e-mail.
print(f"¡Hola {nombre} {apellido}! Registro completado con éxito para el e-mail: {email}")


Nombre = input("ingresa tu nombre:")
Apellido = input("ingresa tu apellido:")
print(Nombre)
print(Apellido)