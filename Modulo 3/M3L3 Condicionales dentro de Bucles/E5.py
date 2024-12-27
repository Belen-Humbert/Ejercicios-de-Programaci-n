import random

contador = 0

# Nivel 1: Números entre 1 y 10
print("¡Bienvenido al Nivel 1! Resuelve sumas con números entre 1 y 10.")
for i in range(5):
    x =       (1, 10)
    y = random.randint(1, 10)
    print("Pregunta", i + 1, ": ¿Cuánto es", x, "+", y, "?")
    respuesta = int(input("Tu respuesta: "))
    
    if respuesta == x + y:
        print("¡Correcto! 🎉")
        contador = contador + 1
    else:
        print("Incorrecto. La respuesta correcta era:", x + y)

print("Has terminado el Nivel 1 con un puntaje de", contador, "de 5")

# Nivel 2: Números entre 1 y 100
print("¡Bienvenido al Nivel 2! Resuelve sumas con números entre 1 y 100.")
for i in range(5):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    print("Pregunta", i + 1, ": ¿Cuánto es", x, "+", y, "?")
    respuesta = int(input("Tu respuesta: "))
    
    if respuesta == x + y:
        print("¡Correcto! 🎉")
        contador = contador + 1
    else:
        print("Incorrecto. La respuesta correcta era:", x + y)

print("¡Has terminado el juego con un puntaje total de", contador, "de 10 🎉")
