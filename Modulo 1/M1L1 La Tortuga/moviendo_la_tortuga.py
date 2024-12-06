# Para empezar a trabajar con la tortuga, primero hay que introducir el siguiente código:
# import turtle
#
# t = turtle.Turtle()
# t.shape("turtle")
#
# Ejecuta el código para ver la tortuga.
#
# Ahora que la tortuga ya ha sido creada, podemos establecer su dirección utilizando los siguientes comandos:
#
# t.forward(100) – la tortuga avanza (la distancia en píxeles se especifica entre paréntesis).
# t.backward(100) – la tortuga retrocede (la distancia en píxeles se indica entre paréntesis).
# t.left(90) – la tortuga gira hacia la izquierda (el ángulo en grados se especifica entre paréntesis).
# t.right(90) – la tortuga gira hacia la derecha (el ángulo en grados se indica entre paréntesis).
#
# Intenta aplicar varios comandos a la tortuga, especificando los valores entre paréntesis.
#
# Con el fin de entender en qué dirección y en cuántos grados debe girar la tortuga, 
# imagina que estás mirando en la misma dirección que la tortuga. Entonces:
# - La dirección en la que estás mirando es de 0 grados.
# - Si extiendes tu mano izquierda hacia la izquierda, estará a 90 grados hacia la izquierda.

# Código:
import turtle 

t = turtle.Turtle()
t.shape("turtle")
t.forward(100)
t.left(90)
t.left(90)
t.forward(100)