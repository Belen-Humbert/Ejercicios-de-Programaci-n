import random

while True:
    # Generar dos números aleatorios entre 1 y 20
    x = random.randint(1, 20)
    y = random.randint(1, 20)

    # Mostrar la pregunta en consola
    print("¿Cuál es la suma de estos números?", x, "+", y)

    # Obtener la respuesta del usuario con manejo de errores
    while True:
        try:
            respuesta_usuario = int(input("Tu respuesta: "))
            break  # Si la conversión es exitosa, salimos del bucle
        except ValueError:
            print("Por favor ingresa un número válido.")

    # Comparar la respuesta del usuario con la respuesta correcta
    if respuesta_usuario == (x + y):
        print("¡Felicitaciones, la respuesta es correcta!")
    else:
        print("Lo siento, la respuesta correcta es:", x + y)

