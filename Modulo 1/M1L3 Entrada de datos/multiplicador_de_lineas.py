# Hoy ya has escrito muchos programas útiles. ¡Ahora es el momento de hacer algo divertido!

# Vamos a crear un robot de spam que envíe un mensaje a la consola tantas veces como el usuario desee.

# Pedimos al usuario que introduzca la palabra o frase que desea generar.
mensaje = input("¿Qué deseas generar? (Escribe una palabra o frase): ")  # Solicitamos la entrada del usuario y la almacenamos en la variable 'mensaje'.

# Pedimos al usuario que introduzca cuántas veces quiere que se genere el mensaje.
cantidad = int(input("¿Cuántas veces deseas generarlo?: "))  # Convertimos la entrada del usuario a un número entero para usarlo en el bucle.

# Generamos el mensaje repetido utilizando la multiplicación de cadenas.
# Multiplicamos la cadena 'mensaje' por el número 'cantidad' y la imprimimos en la consola.
print(mensaje * cantidad)  

# El carácter de ruptura de la cadena, como '\n', puede usarse si queremos que los mensajes aparezcan en líneas separadas.
# Por ejemplo, el siguiente código genera el mensaje en líneas diferentes:
# print((mensaje + '\n') * cantidad)

# ¡Eso es todo! El usuario puede generar cualquier mensaje que desee, tantas veces como quiera.


texto = input("¿Que cadena o palabra deseas generar?\n")
cantidad = int(input("¿Cuantas veces desea general la palabra?\n"))

print(texto * cantidad)