# A veces es necesario generar varios tipos de datos diferentes al mismo tiempo.
# En ese caso, puedes generarlos separados por comas.

# Ejemplo:
# Vamos a declarar dos variables: una para almacenar nuestro nombre y otra para almacenar nuestra edad.
#nombre = "Nombre"  # Aquí asignamos una cadena con el valor "Nombre" a la variable 'nombre'
#edad = 14  # Aquí asignamos un número entero 14 a la variable 'edad'

# Ahora, para generar la información de estas dos variables juntas, utilizamos el comando print().
# El comando 'print()' puede aceptar varios valores, y si los separas por comas, Python los imprimirá con un espacio entre ellos.
#print("Me llamo", nombre, "y tengo", edad, "años")  # Imprime el texto con las variables 'nombre' y 'edad' interpoladas

# En este caso, la salida será: "Me llamo Nombre y tengo 14 años"
# Python maneja diferentes tipos de datos (cadenas, números, etc.) dentro de un solo 'print', separándolos automáticamente con un espacio.

# ¿Has hecho todo? ¡Bien hecho!

# Ahora que ya sabes cómo hacerlo, intenta utilizar un método similar para contar y describir a tus amigos o familia:
# Puedes declarar más variables para almacenar sus nombres y edades, y luego mostrarlas en un solo 'print()'.



nombre = "Juan"
edad = "17 años"
personas= "cuatro personas."
print("Me llamo", nombre, " y tengo", edad, ", mi familia está conformada por", personas, "Mi padre, mi madre, mi hermana y yo")