import turtle
import random

# Configurar la tortuga
t = turtle.Turtle()
t.speed(0)

# Inicializar el largo de la línea y el color
acumulador = 10

# Dibujar el laberinto en bucle
while True:
    # Configurar el color aleatorio utilizando RGB
    t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Dibujar la línea
    t.forward(acumulador)

    # Girar 90 grados
    t.right(90)

    # Aumentar el largo de la línea en 5 píxeles
    acumulador += 5
