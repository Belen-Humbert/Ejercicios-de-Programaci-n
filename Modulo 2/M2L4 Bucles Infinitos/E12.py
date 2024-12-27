import random

# Generar un número aleatorio entre 1 y 10
x = random.randint(1, 10)

# Pedir al usuario que adivine el número
y = int(input('Intenta adivinar el número elegido por la computadora (entre 1 y 10): '))

# Comparar la respuesta del usuario con el número aleatorio
if y == x:
    print("¡Wow, qué buen sentido de la intuición tienes!")
else:
    print("Esta vez no acertaste. El número elegido por la computadora fue:", x)
