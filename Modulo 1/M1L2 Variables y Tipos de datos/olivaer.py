# Este es un gato llamado Oliver y está muy solo. ¡Ayudémosle a hacer algunos amigos!

# En primer lugar, tienes que mostrar al menos un gato en la consola.
# Para ello utilizaremos el comando print(), que se usa para generar texto en la consola.

# Los siguientes comandos imprimen las cadenas que representan a los gatos:
#print(a)  # Esto imprimirá la cadena que tiene asignada la variable 'a', que representaría un gato
#print(c)  # Imprime el gato en la variable 'c'
#print(d)  # Imprime el gato en la variable 'd'
#print(e)  # Imprime el gato en la variable 'e'
#print(f)  # Imprime el gato en la variable 'f'
#print(g)  # Imprime el gato en la variable 'g'

# ¿Cómo hago ahora varios gatos?

# Sabemos que una cadena puede repetirse varias veces multiplicándola por un número determinado.
# Esto nos permite crear múltiples instancias de "gatos" de forma rápida.

# Definimos la variable "count", que almacenará el número de gatos que queremos generar.
count = 5  # Por ejemplo, si "count" tiene el valor 5, vamos a generar 5 gatos

# Usamos el operador '*' para repetir una cadena el número de veces que indique "count".
# Aquí, multiplicamos la cadena (representando al gato) por "count" para generar varios gatos.
#print("gato " * count)  # Esto imprimirá "gato gato gato gato gato " cinco veces

# Esto generará tantos gatos como se especifique en la variable "count".


count = 4

a = "    /\_____/\    "
b = "   /  o   o  \   "
c = "  ( ==  ^  == )  "
d = "   )         (   "
e = "  (           )  "
f = " ( (  )   (  ) ) "
g = "(__(__)___(__)__)"
# Introduce tu código a continuación
print(a * count)
print(b * count)
print(c * count)
print(d * count)
print(e * count)
print(f * count)
print(g * count)