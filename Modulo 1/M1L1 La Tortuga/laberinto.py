# Hoy la tortuga nos ayudó y enseñó mucho, y ahora nos pide ayuda. Se quedó atrás de sus amigos y se perdió.
# ¿Puedes ayudarle a alcanzar a sus amigos?

# Hay algunos comandos que puedes utilizar:

# t.forward(100) – la tortuga se mueve hacia adelante.
# t.backward(100) – la tortuga se mueve hacia atrás.
# t.left(90) – la tortuga gira a la izquierda.
# t.right(90) – la tortuga gira a la derecha.

# Escribir estos comandos cada vez puede ser muy repetitivo y aburrido, es así como puedes acelerar el proceso.
# Muchos comandos para la tortuga tienen versiones abreviadas:

# t.forward(100) = t.fd(100)
# t.backward(100) = t.bk(100)
# t.left(90) = t.lt(90)
# t.right(90) = t.rt(90)

# Ahora desplázate a través del código y encuentra el comentario "Introduce tu código a continuación".
# Puedes empezar a programar la salida del laberinto para la tortuga después de ello.

# ¡Buena suerte! 😉


import turtle

t = turtle.Turtle()
t.shape("turtle")
# No cambies el siguiente código ya que este dibuja un laberinto
t.speed(0)
t.up()
t.goto(-75, 180)
t.down()
t.right(90)
t.forward(35)
t.left(90)
t.forward(70)
t.right(90)
t.forward(35)
t.left(90)
t.forward(35)
t.right(90)
t.forward(35)
t.right(90)
t.forward(35)
t.left(90)
t.forward(70)
t.backward(35)
t.left(90)
t.forward(70)
t.left(90)
t.forward(70)
t.up()
t.goto(-75, 180)
t.down()
t.right(90)
t.forward(105)
t.right(90)
t.forward(35)
t.left(90)
t.forward(70)
t.right(90)
t.forward(70)
t.left(90)
t.forward(35)
t.left(90)
t.forward(35)
t.up()
t.goto(30, 180)
t.down()
t.right(90)
t.forward(105)
t.right(90)
t.forward(35)
t.left(90)
t.forward(35)
t.right(90)
t.forward(105)
t.right(90)
t.forward(70)
t.left(90)
t.forward(70)
t.right(90)
t.forward(35)
t.right(90)
t.forward(35)
t.left(90)
t.forward(35)
t.left(90)
t.forward(35)
t.right(90)
t.forward(35)
t.left(90)
t.forward(70)
t.right(90)
t.forward(35)
t.right(90)
t.forward(105)
t.left(90)
t.forward(35)
t.left(90)
t.forward(35)
t.up()
t.goto(135, 180)
t.down()
t.left(90)
t.forward(70)
t.right(90)
t.forward(35)
t.left(90)
t.forward(70)
t.right(90)
t.forward(35)
t.left(90)
t.forward(35)
t.left(90)
t.forward(35)
t.up()
t.goto(205, 180)
t.down()
t.right(90)
t.forward(140)
t.right(90)
t.forward(245)
t.right(90)
t.forward(140)
t.left(90)
t.forward(35)
t.backward(70)
t.left(90)
t.forward(35)
t.left(90)
t.forward(35)
t.right(90)
t.forward(35)
t.right(90)
t.forward(35)
t.left(90)
t.forward(35)
t.left(90)
t.forward(105)
t.left(90)
t.forward(35)
t.up()
t.goto(320, -80)
t.left(180)
t.color("green")
t.stamp()
t.goto(320, -115)
t.stamp()
t.goto(320, -150)
t.stamp()
t.color("black")
t.goto(205, -135)
t.down()
t.right(180)
t.forward(35)
t.backward(35)
t.left(90)
t.forward(35)
t.right(90)
t.forward(140)
t.right(90)
t.forward(35)
t.right(90)
t.forward(70)
t.left(90)
t.forward(70)
t.right(90)
t.forward(35)
t.right(90)
t.forward(35)
t.backward(35)
t.right(90)
t.forward(35)
t.right(90)
t.forward(35)
t.right(90)
t.forward(35)
t.left(90)
t.forward(35)
t.right(90)
t.forward(35)
t.left(90)
t.forward(105)
t.right(90)
t.forward(35)
t.right(90)
t.forward(70)
t.left(90)
t.forward(35)
t.up()
t.goto(65, -170)
t.down()
t.left(180)
t.forward(35)
t.right(90)
t.forward(105)
t.right(90)
t.forward(70)
t.right(90)
t.forward(35)
t.right(90)
t.forward(35)
t.up()
t.goto(30, -170)
t.down()
t.forward(35)
t.right(90)
t.forward(35)
t.left(90)
t.forward(70)
t.right(90)
t.forward(70)
t.up()
t.goto(-5, -170)
t.down()
t.left(90)
t.forward(105)
t.right(90)
t.forward(35)
t.backward(35)
t.left(90)
t.forward(70)
t.right(90)
t.forward(35)
t.right(90)
t.forward(35)
t.left(90)
t.forward(35)
t.right(90)
t.forward(35)
t.left(90)
t.forward(35)
t.up()
t.goto(-180, -170)
t.down()
t.forward(210)
t.right(90)
t.forward(35)
t.right(90)
t.forward(105)
t.up()
t.goto(-180, 40)
t.down()
t.left(180)
t.forward(35)
t.right(90)
t.forward(105)
t.left(90)
t.forward(35)
t.right(90)
t.forward(35)
t.right(90)
t.forward(70)
t.right(90)
t.forward(70)
t.left(90)
t.forward(70)
t.up()
t.goto(-110, 125)
t.left(90)
t.color("green")
t.down()

t.forward(90)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(70)
t.lt(90)
t.fd(70)
t.lt(90)
t.fd(30)
t.rt(90)
t.fd(70)
t.lt(90)
t.fd(70)
t.lt(90)
t.fd(70)
t.rt(90)
t.fd(110)
t.lt(90)
t.fd(70)
t.rt(90)
t.fd(70)
t.lt(90)
t.fd(100)
t.rt(90)
t.fd(70)
t.rt(90)
t.fd(70)
t.lt(90)
t.fd(30)
t.rt(90)
t.fd(35)
t.rt(90)
t.fd(70)
t.lt(90)
t.fd(30)
t.rt(90)
t.fd(30)
t.lt(90)
t.fd(110)
t.lt(90)
t.fd(80)