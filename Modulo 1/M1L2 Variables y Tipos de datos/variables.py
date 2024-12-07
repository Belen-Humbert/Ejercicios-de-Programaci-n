# Una variable es el contenido de una ubicación de memoria en un computador,
# donde se puede almacenar cualquier dato (números, palabras, frases).
#
# Lo primero que hay que hacer para declarar una variable es asignarle un nombre.
# 
# Por ejemplo, una variable que almacenará tu nombre puede ser declarada como 'nombre',
# y una variable con tu edad puede ser declarada como 'edad'.
# 
# Después, tenemos que asignar un valor a una variable. Puede ser un carácter, una cadena o un número.
# 
# Las cadenas y los caracteres se representan entre comillas:
# nombre = "Nombre"
# Los números y las cifras se representan sin comillas:
# edad = 14
# 
# El código ya tiene una variable y se llama "salto". Encuéntrala y comprueba su valor.
# salto = 10
# ¿De qué crees que es responsable esta variable?
# 
# Prueba cambiando su valor y verifica qué cambia.
# 
# Y luego, especifica la distancia de salto para que la tortuga salte sobre la línea 2🐢
#
# Algunas reglas para las variables:
#
# - Solo puedes utilizar letras latinas, números y guiones bajos (piso);
# - El nombre de una variable no puede empezar por un número;
# - Python distingue entre mayúsculas y minúsculas, lo que significa que las variables abc y aBc son dos variables diferentes;
# - Estarás mucho más cómodo trabajando con el código si el nombre de una variable refleja su propósito.


import turtle

t = turtle.Turtle()
t.shape("turtle")

# El siguiente código no debe ser cambiado :)
t.speed(10)
t.up()
t.forward(10)
t.left(90)
t.down()
t.forward(30)
t.write("1")
t.backward(60)
t.up()
t.goto(0,0)
t.right(90)
t.forward(275)
t.left(90)
t.down()
t.forward(30)
t.write("2")
t.backward(60)
t.up()
t.goto(0,0)
t.right(90)
t.down()
t.color("red")

# Introduce tu código a continuación
salto = 280 # Distancia de salto
t.forward(salto)