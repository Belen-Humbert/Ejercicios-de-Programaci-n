count = 0  # Contador de manzanas añadidas

while True:
    x = int(input("¿Cuántas manzanas debería agregar?: "))
    
    # Sumamos las manzanas añadidas
    count += x
    
    # Verificamos las condiciones
    if count < 12:
        print("Te faltan", 12 - count, "manzanas.")
    elif count == 12:
        print("¡Perfecto! Ya tienes las 12 manzanas necesarias para la tarta.")
        break  # El programa termina
    else:
        print("¡Hay demasiadas manzanas! Has superado las 12 manzanas.")
        break  # El programa termina si hay más de 12 manzanas
