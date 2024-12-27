import random

count = 0  # Contador de puntos
nivel = 1  # Nivel inicial
while True:
    # Dependiendo del nivel, el rango de números cambiará
    if nivel == 1:
        x = random.randint(1, 10)
    else:
        x = random.randint(1, 15)
    
    answer = int(input("Adivina el número: "))
    
    if answer == x:
        if nivel == 1:
           count += 1  # 1 punto por el primer nivel
        else:
            count += 2  # 2 puntos por el segundo nivel
        print("¡Correcto! ¡Punto(s) ganado(s)!")
    else:
        print("Más suerte la próxima.")
    
    seguir = input("¿Quieres seguir jugando? (sí/no): ")
    if seguir == "no":
        break
    elif seguir == "sí" and nivel == 1:

        nivel = 2
        print("¡Pasas al segundo nivel! Los números ahora serán del 1 al 15.")
    
print("Puntaje final:", count)
