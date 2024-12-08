# Hagamos que el registro en nuestro programa sea más detallado: agrega información sobre el nombre de usuario y la contraseña del usuario.

# Mostramos un mensaje inicial explicando que vamos a realizar un registro.
print("¡Bienvenido al sistema de registro! 😊")  

# Solicitamos al usuario que ingrese su nombre.
nombre = input("Introduce tu nombre: ")  # Guardamos el nombre en la variable `nombre`.

# Solicitamos al usuario que ingrese su apellido.
apellido = input("Introduce tu apellido: ")  # Guardamos el apellido en la variable `apellido`.

# Solicitamos al usuario que elija un nombre de usuario.
nombre_usuario = input("Elige un nombre de usuario: ")  # Guardamos el nombre de usuario en la variable `nombre_usuario`.

# Solicitamos al usuario que elija una contraseña.
contrasena = input("Elige una contraseña: ")  # Guardamos la contraseña en la variable `contrasena`.

# Mostramos el mensaje de registro exitoso al usuario, reemplazando las variables en el texto.
print(f"¡Hola {nombre} {apellido}! Tu registro fue completado con éxito.")  # Mostramos el nombre y apellido ingresados.
print(f"Tu nombre de usuario: {nombre_usuario}")  # Mostramos el nombre de usuario.
print(f"Tu contraseña: {contrasena}")  # Mostramos la contraseña seleccionada.

# Finalizamos el programa con un mensaje de confirmación.
print("¡Gracias por registrarte! 😊")  


nombre = input("Introduce un nombre: ")
apellido = input("Introduce tu apellido: ")
usuario = input("Ingresa tu nombre de usuario: ")
contra = input("Ingresa tu contraseña: ")

print("¡Hola", nombre, apellido,"!", "Tu registro fue completado con éxito.")
print("Tu nombre de usuario:", usuario)
print("Tu contraseña:", contra)