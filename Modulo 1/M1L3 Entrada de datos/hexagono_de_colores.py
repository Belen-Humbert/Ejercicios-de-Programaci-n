# ¡Ya es hora de dibujar! 

# Importamos la librería turtle para poder dibujar el hexágono.
import turtle  

# Mostramos un mensaje inicial explicando la funcionalidad del programa.
print("Este programa dibuja un hexágono personalizado. 🎨")  

# Pedimos al usuario que ingrese el color del contorno del hexágono.
contorno = input("Introduce el color del contorno: ")  # Almacenamos el color del contorno en la variable `contorno`.

# Pedimos al usuario que ingrese el color del relleno del hexágono.
relleno = input("Introduce el color de relleno: ")  # Almacenamos el color de relleno en la variable `relleno`.

# Pedimos al usuario que introduzca el tamaño de los lados del hexágono.
tamanio = int(input("Introduce el tamaño de los lados (en píxeles): "))  # Convertimos la entrada en un entero y la almacenamos en `tamanio`.

# Configuramos el color del contorno del hexágono usando el método `pencolor()` de turtle.
turtle.pencolor(contorno)  

# Configuramos el color de relleno del hexágono usando el método `fillcolor()` de turtle.
turtle.fillcolor(relleno)  

# Comenzamos a llenar el hexágono con el color seleccionado.
turtle.begin_fill()  

# Usamos un bucle para dibujar los 6 lados del hexágono.
for _ in range(6):  # Repetimos el siguiente bloque de código 6 veces.
    turtle.forward(tamanio)  # Dibujamos un lado del hexágono del tamaño especificado por el usuario.
    turtle.left(60)  # Giramos 60 grados hacia la izquierda para formar el ángulo correcto del hexágono.

# Finalizamos el relleno del hexágono.
turtle.end_fill()  

# Mostramos un mensaje final indicando que el hexágono se ha dibujado.
print("¡Hexágono dibujado con éxito! 🖌️")  

# Mantenemos la ventana abierta para que el usuario pueda ver el hexágono.
turtle.done()  


import turtle

t = turtle.Turtle()
t.shape("turtle")
# Escribe tu código a continuación 
color1 = input ("Introduce el 1er color:")
color2 = input ("Introduce el 2do color:")
distance = int(input("introduce la distancia"))

t.color(color1)
t.forward(distance)
t.left(60)
t.forward(distance)
t.left(60)
t.forward(distance)
t.color(color2)
t.left(60)
t.forward(distance)
t.left(60)
t.forward(distance)
t.left(60)
t.forward(distance)
t.left(60)