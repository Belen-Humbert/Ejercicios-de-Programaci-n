count_n = 0  # Contador de números negativos
count_p = 0  # Contador de números positivos

while True:
    x = int(input("Ingresa un número (o escribe 0 para terminar): "))
    
    if x > 0:
        count_p += 1  # Incrementar el contador de positivos
    elif x < 0:
        count_n += 1  # Incrementar el contador de negativos
    else:
        print("Esto es cero")
        break  # Finalizar el bucle si el número es cero
