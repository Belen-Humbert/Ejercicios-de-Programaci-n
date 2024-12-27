import turtle
import random

t = turtle.Turtle()

while True:
    angle = int(input("Ingresa un ángulo (0 para detenerse): "))
    
    if angle == 0:
        print("El programa ha terminado.")
        break  # Detener el programa si el ángulo es 0
    
    distance = random.randint(10, 50)
    
    # La tortuga gira con el ángulo ingresado
    t.right(angle)
    
    # La tortuga dibuja una línea con la longitud aleatoria
    t.forward(distance)
