count = 0  # Contador de candidatos seleccionados

for i in range(5):
    print("Candidato", i + 1)
        age = int(input("Ingresa tu edad: "))  
        pr = input("¿Te gusta programar? (sí/no): ") 
        experience = int(input("¿Cuántos años de experiencia laboral tienes? "))  
        
        # Separar las condiciones en pasos claros
        cumple_edad = 12 <= age <= 17
        le_gusta_programar = pr == "sí"
        tiene_experiencia = experience > 2
        
        # Verificar si cumplen con los requisitos
        if cumple_edad and le_gusta_programar and tiene_experiencia:
            print("¡Felicidades! Has sido seleccionado para el equipo.")
            count += 1
        else:
            print("Lo sentimos, no cumples con los requisitos para unirte al equipo.")

print("¡El proceso de selección ha finalizado!")
print("Se seleccionaron", count, "candidatos.")
