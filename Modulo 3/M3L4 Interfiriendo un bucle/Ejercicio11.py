import random

count = 0

while True:
    x = random.randint(0, 100)
    count += 1  # Aumentamos el contador por cada número generado
    
    if x == 73:
        break  # Detenemos el bucle cuando el número es 73

print("El número 73 fue generado después de", count, "intentos.")
