# Inicializar el número máximo con un valor muy bajo
max = 0

# Pedir 5 números al usuario
for i in range(5):
    x = int(input("Ingrese el número {i + 1}: "))
    if x > max:
        max = x  # Actualizar el valor máximo si el número ingresado es mayor

# Mostrar el número más grande ingresado
print("El número más grande ingresado es:", max)


