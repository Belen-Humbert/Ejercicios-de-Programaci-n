# Inicializar sumas
suma_positivos = 0
suma_negativos = 0

# Bucle para recibir 5 números
for i in range(5):
    numero = int(input("Ingrese el número {i + 1}: "))

    # Verificar si el número es positivo o negativo
    if numero > 0:
        suma_positivos += numero
    else:
        suma_negativos += numero

# Mostrar los resultados
print("\nResultados:")
print("Suma de números positivos:", suma_positivos)
print("Suma de números negativos:", suma_negativos)
