import time
import random

# Bucle infinito para seguir generando contraseñas
while True:
    # Solicitar el nombre de usuario
    registro = input('Ingresa tu nombre de usuario: ')
    
    # Generar una contraseña aleatoria entre 1000 y 100000
    contraseña = random.randint(1000, 100000)
    
    # Retrasar 5 segundos antes de mostrar la contraseña
    print("Generando tu contraseña...")
    time.sleep(5)
    
    # Mostrar la contraseña generada
    print("Hola", registro, "tu contraseña es:", contraseña)
    
    # Preguntar si desea continuar generando contraseñas
    continuar = input("¿Quieres generar otra contraseña? (sí/no): ")
    if continuar == 'no':
        print("¡Hasta luego!")
        break

