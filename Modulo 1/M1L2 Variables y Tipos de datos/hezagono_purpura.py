# Ahora, utilizaremos la tortuga para dibujar un hexágono inusual.

# ¿Por qué es inusual?
# Porque tendrá dos tamaños de lados: tres lados serán más grandes y tres más pequeños.
# Además, los lados de diferentes tamaños se alternarán, lo que le da un aspecto único.

# En primer lugar, vamos a establecer el color del hexágono como púrpura.
# Para ello, utilizaremos el comando t.color() de la tortuga.

# Luego, necesitaremos declarar las variables necesarias:
# side1: longitud de los lados grandes.
# side2: longitud de los lados pequeños.
# angle: grados de rotación que la tortuga debe realizar para dibujar cada lado del hexágono.

# Establecemos los valores de las variables:
side1 = 100  # Lados grandes de tamaño 100 unidades.
side2 = 50   # Lados pequeños de tamaño 50 unidades.
angle = 60   # Ángulo de rotación para cada vértice del hexágono (60 grados para un hexágono regular).

# Ahora, utilizaremos el código de la tortuga para dibujar el hexágono con los lados alternados.
# Comenzamos con el lado grande, luego alternamos con el lado pequeño, y así sucesivamente.

import turtle

# Inicializamos la tortuga.
t = turtle.Turtle()

# Establecemos el color de la tortuga (hexágono púrpura).
t.color("purple")

# Dibujamos el hexágono alternando los lados grandes y pequeños.
for _ in range(3):  # Hacemos 3 repeticiones para los lados grandes.
    t.forward(side1)  # Dibujamos el lado grande.
    t.left(angle)      # Rotamos 60 grados.
    
    t.forward(side2)  # Dibujamos el lado pequeño.
    t.left(angle)      # Rotamos 60 grados.

# Finalizamos el dibujo.
turtle.done()

# Explicación:
# 1. Usamos la función t.color() para hacer que el hexágono sea de color púrpura.
# 2. La variable 'side1' se usa para los lados grandes y 'side2' para los pequeños.
# 3. La tortuga dibuja un lado grande, luego uno pequeño, alternando con cada iteración del ciclo.
# 4. El ángulo de rotación entre los lados es de 60 grados (común en los hexágonos).
# 5. Finalmente, mostramos el hexágono en la pantalla.

# Resultado esperado:
# Un hexágono púrpura donde tres lados son largos y tres cortos, alternándose entre sí.

import turtle

t = turtle.Turtle()
t.shape("turtle")

side1 = 150
side2 = 50
angle = 60

# Introduce tu código a continuación
t.color("purple")
t.forward(side2)
t.right(angle)
t.forward(side1)

t.right(angle)
t.forward(side2)
t.right(angle)
t.forward(side1)

t.right(angle)
t.forward(side2)
t.right(angle)
t.forward(side1)
