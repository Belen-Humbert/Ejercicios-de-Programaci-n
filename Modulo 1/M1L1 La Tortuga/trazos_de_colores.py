# Para no olvidar todos estos nuevos comandos que hemos aprendido, pongámoslos en práctica.

# Te sugiero que hagas un dibujo similar (puedes elegir los colores que quieras).

# Si ejecutas el código, verás que ya se han dibujado un trazo visible y otro invisible.
# Ahora solo tenemos que crear 2 trazos más de color. Para lo cual, puedes seguir estos consejos:

# Para establecer el color de la tortuga, utiliza el siguiente código:
# t.color("green")

# Para dibujar una línea visible de 20 píxeles, utiliza el siguiente código:
# t.forward(20)

# Para dibujar una línea invisible de 20 píxeles, utiliza el siguiente código:
# t.up()      # Detiene el dibujo del rastro
# t.forward(20)
# t.down()    # Reactiva el rastro

# Así, puedes crear trazos visibles e invisibles, controlando el color y la visibilidad del rastro de la tortuga.

import turtle

t = turtle.Turtle()
t.shape("turtle")

t.color("yellow")
t.forward(20)
t.up()
t.forward(20)
t.down()

t.color("red")
t.forward(20)
t.up()
t.forward(20)
t.down()

t.color("cyan")
t.forward(20)
t.up()
t.forward(20)
t.down()