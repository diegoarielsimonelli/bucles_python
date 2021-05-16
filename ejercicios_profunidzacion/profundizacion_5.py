# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Tome el ejercicio:
<condicionales_python / ejercicios_profundizacion / profundizacion_4>,
copielo a este ejercicio y modifíquelo para cumplir
el siguiente requerimiento

Realize un programa que corra indefinidamente en un bucle, al comienzo de la
iteración del bucle el programa consultará al usuario con el siguiente menú:
1 - Obtener la palabra más grande por orden alfabético (usando el operador ">")
2 - Obtener la palabra más grande por cantidad de letras (longitud de la palabra)
3 - Salir del programa

En caso de presionar "3" el programa debe terminar e informar por
pantalla de que ha acabado,
en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea

NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
un mensaje de error y volver a comenzar el bucle
(vea en el apunte "Bucles - Sentencias" para encontrar
la sentencia que lo ayude a cumplir esa tarea)

Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
en donde en cada iteración se pedirá una palabra. La cantidad de iteración
(cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
condición esté dada por una variable (ej: palabras_deseadas = 4)
Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
Luego de tener las palabras deseadas almacenadas en una lista de palabras
se debe proceder a realizar las siguientes tareas:

Si se ingresa "1" por consola se debe obtener la palabra
más grande por orden alfabético
Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
se debe imprimir en pantalla cual era la palabra
más grande alfabeticamente.
Recuerde que debe inicializar primero su variable
donde irá almacenando la palabra que cumpla dicha condición.
¿Con qué valor debería ser inicializada dicha variable?

Si se ingresa "2" por consola se debe obtener la palabra
con mayor cantidad de letras
Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
se debe imprimir en pantalla cual era la palabra con
mayor cantidad de letras.
Recuerde que debe inicializar primero su variable
donde irá almacenando la palabra que cumpla dicha condición.
¿Con qué valor debería ser inicializada dicha variable?

NOTA: No se debe ordenar la lista de palabras, se debe obtener
el máximo utilizando el mismos métodos vistos durante la clase
(ejemplos_clase), tal como el ejercicio anterior. Ordenar una
lista representa un problema mucho más complejo que solo
buscar el máximo.

NOTA: Es recomendable que se organice con lápiz y papel para
hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
    que se deben ir guardando en una lista
3- Otro bucle interno que corre luego de que termine el bucle "2" que
    recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")
'''

print("Mi primer pasito en data analytics")
# Empezar aquí la resolución del ejercicio





while True:
    palabras_alfabeto=None
    palabras_letras= None
    palabras_deseadas = 4
    palabras = []

    print("¿Cómo quieres ordenar las 4 palabras?\n Hay 3 opciones: 1,2 ó 3: \n 1 - Obtener la palabra más grande por orden alfabético \n 2 - Obtener la palabra más grande por cantidad de letras \n 3 - Salir del programa")
    opción= (input())
    print("la opción elegida es:",opción)
    if opción == 1:
        for i in range(palabras_deseadas):  
            print("Dígame una palabra", str(i + 1) + ": ", end="")
            palabra =(input())
            palabras.apped(palabra)
            print("La lista creada es:", palabras)
        for palabra in palabras:
            if (palabras_alfabeto == None) or (palabras_alfabeto < palabra):
                palabras_alfabeto = palabra
                print(palabras_alfabeto, "es la mayor palabra ordenando alfabéticamente")
    elif opción == 2:
        for i in range(palabras_deseadas):
            print("Dígame una palabra", str(i + 1) + ": ", end="")
            palabra =(input())
            palabras.apped(palabra)
            print("La lista creada es:", palabras)
            
        for palabra in palabras:
            if (palabras_letras == None) or (len(palabras_letras) < len(palabra)):
                palabras_letras = palabra
                print("la palabra con mayor cantidad de letras es:", palabras_letras)

    elif opción == 3:
        print("el programa finalizó")
        break

    else: 
        print("Error.Los valores validos son: 1,2 y 3. Pruebe de nuevo")
        
        
        

        
    

    
