# Con la ayuda de la función input(), incluso el problema más simple puede volverse más interesante y útil.

# Importamos el módulo turtle para dibujar con la tortuga.
import turtle  

# Creamos una instancia de la tortuga.
t = turtle.Turtle()  

# Pedimos al usuario que introduzca un color para la tortuga.
color1 = input("Introduce el color de la tortuga: ")  # El usuario elige el color de la tortuga.

# Pedimos al usuario que introduzca la distancia que debe recorrer la tortuga.
distancia = int(input("Introduce la distancia que recorrerá la tortuga: "))  # Convertimos la entrada a un número entero.

# Pedimos al usuario que introduzca el ángulo de rotación para la tortuga.
angulo = int(input("Introduce el ángulo de rotación: "))  # Convertimos la entrada a un número entero.

# Asignamos el color elegido por el usuario a la tortuga.
t.color(color1)  # Establecemos el color de la tortuga.

# Dibujamos una figura de cinco lados con los parámetros ingresados.
for _ in range(5):  # Repetimos 5 veces para dibujar 5 lados.
    t.forward(distancia)  # La tortuga se mueve hacia adelante una distancia especificada por el usuario.
    t.left(angulo)  # La tortuga gira a la izquierda con un ángulo especificado por el usuario.

# Cerramos la ventana de dibujo al hacer clic.
turtle.done()  

# Si queremos dibujar una estrella, el ángulo de rotación adecuado sería de 144 grados.
# El valor del ángulo de rotación para dibujar una estrella es 144.


import turtle

t = turtle.Turtle()
t.shape("turtle")
# Introduce tu código a continuación
color1 = input("ingresa el color:")
distance = int(input("introduce la distancia"))
angle = int(input("introduce el angulo"))

t.color(color1)
t.forward(distance)
t.left(angle)
t.forward(distance)
t.left(angle)
t.forward(distance)
t.left(angle)
t.forward(distance)
t.left(angle)
t.forward(distance)
t.left(angle)

# Calculé el valor del ángulo de rotación y es igual a: (resultado)
145