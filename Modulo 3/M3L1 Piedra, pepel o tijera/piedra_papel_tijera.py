import random
import time

MiPuntaje = 0
PuntajeCompu = 0

print("¡Bienvenido al juego Piedra, Papel o Tijera!")
print("Reglas: Piedra aplasta Tijeras, Tijeras cortan Papel, Papel cubre Piedra.")

while True:
    # Elección del jugador
    jugador = input("\nElige (piedra, papel, tijeras o salir): ").lower()
    if jugador == "salir":
        print("¡Gracias por jugar!")
        break

    if jugador not in ["piedra", "papel", "tijeras"]:
        print("Entrada no válida. Por favor, elige 'piedra', 'papel' o 'tijeras'.")
        continue

    # Elección de la computadora
    opciones = ["piedra", "tijeras", "papel"]
    compu = opciones[random.randint(0, 2)]

    # Cuenta regresiva
    print("Piedra...")
    time.sleep(1)
    print("Papel...")
    time.sleep(1)
    print("Tijeras...")
    time.sleep(1)
    print("¡1, 2, 3! La computadora eligió: {}.".format(compu))

    # Determinar el ganador
    if jugador == compu:
        print("¡Es un empate!")
    elif (jugador == "piedra" and compu == "tijeras") or \
         (jugador == "tijeras" and compu == "papel") or \
         (jugador == "papel" and compu == "piedra"):
        print("¡Ganaste esta ronda!")
        MiPuntaje += 1
    else:
        print("La computadora gana esta ronda.")
        PuntajeCompu += 1

    # Mostrar puntuación
    print("Puntuación: Tú {} - Computadora {}".format(MiPuntaje, PuntajeCompu))

print("\nJuego terminado. Resultado final:")
print("Tú: {} - Computadora: {}".format(MiPuntaje, PuntajeCompu))
if MiPuntaje > PuntajeCompu:
    print("¡Felicidades, ganaste el juego!")
elif MiPuntaje < PuntajeCompu:
    print("La computadora ganó el juego. ¡Mejor suerte la próxima vez!")
else:
    print("¡Es un empate total!")

