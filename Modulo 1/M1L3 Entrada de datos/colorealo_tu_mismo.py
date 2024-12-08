# Le pediremos al usuario que introduzca dos colores.

# Solicitamos al usuario que introduzca el color de relleno y lo guardamos en la variable 'color1'.
color1 = input("Introduce el color de relleno: ")

# Solicitamos al usuario que introduzca el color del contorno y lo guardamos en la variable 'color2'.
color2 = input("Introduce el color del contorno: ")

# Importamos el módulo turtle para dibujar la figura.

# Inicializamos la tortuga.
t = turtle.Turtle()

# Establecemos el color de relleno utilizando la variable 'color1'.
t.fillcolor(color1)

# Establecemos el color del contorno utilizando la variable 'color2'.
t.pencolor(color2)

# Comenzamos el relleno de la figura.
t.begin_fill()

# Dibujamos el diamante:
# Movemos la tortuga hacia adelante 100 unidades.
t.forward(100)

# Giramos la tortuga 120 grados a la izquierda.
t.left(120)

# Movemos la tortuga hacia adelante 100 unidades.
t.forward(100)

# Giramos la tortuga 120 grados a la izquierda.
t.left(120)

# Movemos la tortuga hacia adelante 100 unidades para cerrar el triángulo superior.
t.forward(100)

# Giramos la tortuga 60 grados a la derecha para comenzar el triángulo inferior.
t.right(60)

# Movemos la tortuga hacia adelante 100 unidades para el primer lado del triángulo inferior.
t.forward(100)

# Giramos la tortuga 120 grados a la derecha.
t.right(120)

# Movemos la tortuga hacia adelante 100 unidades para el segundo lado del triángulo inferior.
t.forward(100)

# Giramos la tortuga 120 grados a la derecha.
t.right(120)

# Movemos la tortuga hacia adelante 100 unidades para cerrar el triángulo inferior.
t.forward(100)

# Finalizamos el relleno de la figura.
t.end_fill()

# Finalizamos el programa y mostramos el dibujo en la pantalla.
turtle.done()

# Explicación general:
# 1. Solicitamos al usuario los colores para personalizar el dibujo.
# 2. Utilizamos los colores proporcionados con los métodos fillcolor() para el relleno y pencolor() para el contorno.
# 3. Dibujamos un diamante compuesto por dos triángulos equiláteros conectados.
# 4. Comenzamos y terminamos el relleno con begin_fill() y end_fill().
# 5. Al final, mostramos el diamante con los colores elegidos.

import turtle

t = turtle.Turtle()
t.shape("turtle")
# Escribe tu código a continuación
color1 = input("ingresa el color para el relleno:")
color2 = input("ingresa el color para el contorno:")
t.color(color2)
t.pencolor(color1)

t.left(60)
t.forward(80)
t.left(120)
t.forward(83)
t.backward(83)
t.right(120)
t.left(70)
t.forward(15)
t.left(50)
t.forward(65)
t.left(50)
t.forward(15)
t.goto(0,0)
