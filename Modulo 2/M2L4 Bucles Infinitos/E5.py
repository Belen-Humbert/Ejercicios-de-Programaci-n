import random

# Generar un número aleatorio entre 1 y 6
numero = random.randint(1, 6)

# Verificar el resultado
if numero == 5 or numero == 6:
    print("¡Escapaste de los monstruos!")
else:
    print("Esta vez no pudiste escapar, fuiste atrapado por los monstruos…")
