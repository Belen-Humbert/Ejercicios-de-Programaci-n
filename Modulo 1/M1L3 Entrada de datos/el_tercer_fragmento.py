# Ejecuta el programa y mira lo que sucede. El código le pedirá al usuario que ingrese un color y dibuje dos hexágonos de diferentes colores.

# Deberás corregir el código.

# Primero, debes dibujar un tercer hexágono para que el dibujo se vea así:

# En segundo lugar, debes corregir el código para que el programa solicite al usuario los tres colores y el tamaño del lado del hexágono.


import turtle

t = turtle.Turtle()
t.shape("turtle")
t.right(45)

# Variables
color1 = input ("Color 1:")
color2 = input ("Color 2:")
color3 = input ("Color 3:")
size = 100

# El primer hexágono
t.color(color1)
t.forward(size)
t.left(60)
t.forward(size)
t.left(60)
t.forward(size)
t.left(60)
t.forward(size)
t.left(60)
t.forward(size)
t.left(60)
t.forward(size)
t.left(60)

# El segundo hexágono
t.color(color2)
t.forward(size)
t.right(60)
t.forward(size)
t.right(60)
t.forward(size)
t.right(60)
t.forward(size)
t.right(60)
t.forward(size)
t.right(60)
t.forward(size)

# Escribe tu código a continuación
t.color(color3)
t.left(60)
t.forward(size)
t.left(60)
t.forward(size)
t.left(60)
t.forward(size)
t.left(60)
t.forward(size)
t.left(60)
t.forward(size)
t.left(60)
t.forward(size)