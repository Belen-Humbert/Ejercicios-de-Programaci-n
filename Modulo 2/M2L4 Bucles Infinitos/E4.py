import turtle
import random

# Crear la tortuga
t = turtle.Turtle()
t.speed(0)

while True:
    # Generar largo, ángulo y color aleatorios
    largo = random.randint(10, 100)
    angulo = random.randint(10, 360)

    # Generar un color aleatorio en formato RGB (valores entre 0 y 255)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    # Cambiar el color de la tortuga para cada iteración
    t.color(red, green, blue)
    
    # Mover la tortuga
    t.forward(largo)
    t.right(angulo)
