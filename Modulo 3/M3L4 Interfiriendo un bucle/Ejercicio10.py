count = 0

while True:
    x = int(input("Ingresa un número: "))
    
    if x == 0:
        break  # Si el número es 0, detiene el bucle
    
    count += x  # Sumar el número a la variable count

print("La suma total es:", count)
