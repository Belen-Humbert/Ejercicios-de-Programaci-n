import random
import turtle

t = turtle.Turtle()

while True:
    # Preguntamos al usuario la longitud de la línea
    length = int(input("¿Qué longitud debe tener la línea? (ingresa 0 para detenerte): "))
    
    # Si el usuario ingresa 0, detenemos el programa
    if length == 0:
        print("El programa ha terminado.")
        break
    
    # Dibujamos la línea con la longitud proporcionada
    t.forward(length)
    
    # Generamos un ángulo aleatorio entre 1 y 360 grados
    angle = random.randint(1, 360)
    
    # Rotamos la tortuga por el ángulo aleatorio
    t.right(angle)
