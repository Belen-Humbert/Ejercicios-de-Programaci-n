import turtle
import random

t = turtle.Turtle()
contador = 0

# Juego de 3 rondas
for i in range(3):
    # Generar un radio aleatorio entre 20 y 30
    radio = random.randint(20, 30)
    
    # Dibujar el círculo
    t.penup()
    t.goto(0, -radio)  # Mover el círculo hacia abajo para centrarlo
    t.pendown()
    t.circle(radio)
    
    # Preguntar al usuario por el radio
    mensaje = "¿Cuál es el radio del círculo (Partida {i + 1})?"
    respuesta = int(input(mensaje))  # Usar input en lugar de turtle.textinput()
    
    # Verificar si la respuesta es correcta
    t.clear()
    if respuesta == radio:
        t.write("¡Correcto! 🎉", align="center", font=("Arial", 16, "normal"))
        contador += 1
    else:
        t.write("Incorrecto. El radio era: {radio}", align="center", font=("Arial", 16, "normal"))
    
    # Pausa para que el usuario vea el resultado antes de la siguiente ronda
    t.clear()

# Mostrar el puntaje final
t.penup()
t.goto(0, 0)
t.write("¡Juego terminado! Tu puntaje final es:", {contador / 3})
