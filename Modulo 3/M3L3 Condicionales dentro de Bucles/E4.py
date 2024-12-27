contador = 0
chicos = 0
chicas = 0

# Evaluamos a un máximo de 5 postulantes
for i in range(5):
    print("Postulante", i + 1)
    edad = int(input("¿Cuál es tu edad? "))
    genero = input("¿Eres chico o chica? (Responde 'chico' o 'chica'): ")

    # Verificamos si cumple los requisitos de edad
    if 10 <= edad <= 12:
        print("¡Felicitaciones, fuiste admitido al equipo!")
        contador += 1
        if genero == "chico":
            chicos += 1
        elif genero == "chica":
            chicas += 1
    else:
        print("Lamentablemente, no cumples los requisitos.")

# Resultados finales
print("\nResultados finales:")
print("Total de admitidos:", contador)
print("Chicos admitidos:", chicos)
print("Chicas admitidas:", chicas)

