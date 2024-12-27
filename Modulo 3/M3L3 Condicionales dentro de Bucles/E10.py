# Inicializar contador
contador = 0

# Pedir 5 números al usuario
for i in range(5):
    x = int(input("Ingrese el número {i + 1}: "))
    if x < 0:
        contador += 1  # Incrementar el contador si el número es negativo

# Mostrar la cantidad de números negativos ingresados
print("Se ingresaron", contador, "números negativos.")
