import turtle
import random

# Configuración inicial
t = turtle.Turtle()
t.speed(0)  # Configura la velocidad de la tortuga a la máxima
t.color(200, 130, 70)  # Establecer el color usando RGB

i = 1  # Valor inicial del radio

# Bucle infinito
while True:
    t.circle(i)  # Dibuja un círculo con el radio actual
    i += 3  # Aumenta el radio en 5 unidades
    t.right(15)  # Gira un poco para evitar que los círculos se superpongan

