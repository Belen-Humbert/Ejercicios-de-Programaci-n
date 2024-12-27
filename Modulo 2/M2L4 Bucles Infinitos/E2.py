import turtle

t = turtle.Turtle()
t.speed(0)
t.color('seagreen')

# Inicializamos el acumulador
largo = 10  # Largo inicial de la línea
angulo = 45  # Ángulo de giro

while True:  # Bucle infinito
    t.forward(largo)  # Dibuja una línea recta
    t.right(angulo)  # Gira en el ángulo especificado
    largo += 1  # Incrementa el largo de la línea
