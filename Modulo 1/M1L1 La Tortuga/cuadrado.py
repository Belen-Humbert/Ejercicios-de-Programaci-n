# El código listo para usar te permite dibujar un lado de 50 píxeles de un cuadrado 
# y girar en 90 grados a la izquierda.
# t.forward(50)
# t.left(90)
#
# Un lado no es suficiente para un cuadrado completo☺
# Así que, copiemos estas dos líneas de código, insertémoslas bajo el comentario 
# y veamos qué ocurre.
#
# ¿Obtuviste la mitad de un cuadrado? ¡Genial!
#
# A continuación, añade estas líneas de código dos veces más para obtener un cuadrado completo 
# con lados de 50 píxeles☺
#
# Ahora vamos a intentar aumentar el tamaño del cuadrado a 100 píxeles. 
# ¿En qué comandos, desde tu punto de vista, hay que cambiar los valores para esto?

# Código para dibujar un cuadrado:
import turtle

t = turtle.Turtle()
t.shape("turtle")

t.forward(50) 
t.right(90) 
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)