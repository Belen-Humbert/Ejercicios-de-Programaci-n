import time

# Pedimos al usuario el número desde el cual quiere comenzar la cuenta regresiva
num = int(input("¿Desde qué número deseas comenzar el conteo? "))

# Hacemos la cuenta regresiva
for i in range(num, -1, -1):  # Rango descendente desde num hasta 0 (inclusive)
    print(i)  # Mostramos el número actual
    time.sleep(1)  # Pausamos por 1 segundo

print("¡Cuenta regresiva terminada!")
