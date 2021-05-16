# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos con bucles "for"

# Dado la siguiente lista de colores, utilizar "for"
# para imprimir en pantalla todos los colores
colores = ['rojo', 'naranja', 'verde', 'azul']

for x in colores:
    print(x) 

# Itere el "for" utilizando la lista como parámero
# y utilizar como elemento del "for" cada color
# for color ...
for x in colores[0]:
    print(x)
for x in colores[1]:
    print(x)
for x in colores[2]:
    print(x)
for x in colores[3]:
    print(x)
# Itere el "for" utilizando el tamaño de la lista
# como parámetro y utilizar el índice para acceder a
# los elementos de la lista
# for i ...
color= len(colores)

for i in range(color):
    print("El índice",i," color:", colores[i])
    
           
    
    
print("terminamos!")