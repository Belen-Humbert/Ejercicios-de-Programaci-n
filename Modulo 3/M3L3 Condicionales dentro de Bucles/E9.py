import turtle

# Inicializar la tortuga
t = turtle.Turtle()

# Función para dibujar un triángulo
def dibujar_triangulo(t, distancia):
    for i in range(3):
        t.forward(distancia)
        t.left(120)

# Dibujar tres triángulos
for i in range(1, 4):
    # Preguntar al usuario por el tamaño de las líneas
    distancia = int(input("Ingrese el largo de las líneas para el triángulo {i} (entre 1 y 99): "))

    # Validar el tamaño ingresado
    if 0 < distancia < 100:
        dibujar_triangulo(t, distancia)
        t.penup()  # Mover la tortuga sin dibujar
        t.goto(t.xcor() + 150, t.ycor())  # Posición para el próximo triángulo
        t.pendown()
    else:
        t.penup()
        t.goto(0, 0)  # Mostrar mensaje de error en el centro
        t.write("Error: El valor debe estar entre 1 y 99.", align="center", font=("Arial", 16, "normal"))
        t.goto(0, -20)  # Mover la tortuga para evitar solapar texto

# Evitar que la ventana se cierre automáticamente
turtle.done()
