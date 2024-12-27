import time
import random

# Introducción de la historia
print("Después de una larga travesía, llegas a un sitio donde hay dos cuevas...")
time.sleep(2)
print("En una de ellas hay un dragón amistoso que va a compartir sus tesoros contigo...")
time.sleep(2)
print("En la otra cueva vive otro dragón codicioso y hambriento. ¡Si te ve, te comerá!")
time.sleep(2)

# Preguntar al jugador en qué cueva quiere entrar
print("\n¿A qué cueva deseas ir?")
print("1. Cueva 1")
print("2. Cueva 2")

# Obtener la elección del jugador
eleccion = input("Elige la cueva (1 o 2): ")

# Determinar en qué cueva se encuentra el dragón amistoso
cueva_amistosa = random.randint(1, 2)

# Pausa para aumentar la emoción
time.sleep(2)

# Historia según la elección
print("Te vas acercando lentamente a la cueva...")
time.sleep(2)
print("Se ve oscura y escalofriante...")
time.sleep(2)
print("¡De repente, un enorme dragón aparece en frente tuyo! Comienza a abrir su boca y...")

# Verificar si el jugador eligió la cueva correcta
if int(eleccion) == cueva_amistosa:
    time.sleep(2)
    print("¡Felicitaciones! El dragón amistoso te ve y, en lugar de devorarte, te comparte su tesoro!")
else:
    time.sleep(2)
    print("¡Oh no! El dragón codicioso te ve y... ¡te ha devorado! Mejor suerte la próxima vez...")


