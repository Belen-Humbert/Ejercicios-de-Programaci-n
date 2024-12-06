# La tortuga dejará de dibujar si utilizas el siguiente comando:
# t.up() 
# Sí, dejamos los paréntesis vacíos.

# El comando t.up() le dice a la tortuga que ya no necesita dejar un rastro,
# lo que significa que todos sus movimientos pasarán desapercibidos.

# ¿Cómo podemos ahora recuperar el rastro de la tortuga?
# Para hacer esto, usa el siguiente comando:
# t.down() 
# Y de nuevo, los paréntesis están vacíos ☺

# Usando el comando t.down(), puedes decirle a la tortuga que todos los movimientos
# posteriores dejarán rastros.

# Ejecuta el código y observa qué tipo de dibujo hará la tortuga.

# Las acciones que se escriben entre los comandos t.up() y t.down() no dejan ningún rastro.


import turtle

t = turtle.Turtle()
t.shape("turtle")

t.forward(20)
t.up()
t.forward(20)
t.right(30)
t.forward(20)
t.right(30)
t.forward(20)
t.right(30)
t.down()
t.forward(30)