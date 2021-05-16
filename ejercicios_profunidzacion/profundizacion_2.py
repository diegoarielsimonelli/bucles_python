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
Tome el ejercicio de clase:
<condicionales_python /  ejercicios_profundizacion / profundizacion_3.py>,
copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
indefinidamente hasta que como operador se ingrese la palabra "FIN",
en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".


Enunciado:

Realice una calculadora:

Dentro de un bucle se debe ingresar por línea de comando dos números

Luego se ingresará como tercera entrada al programa el símbolo de la operación

que se desea ejecutar:

- Suma (+)

- Resta (-)

- Multiplicación (*)

- División (/)

- Exponente/Potencia (**)

Se debe efectuar el cálculo correcto según la operación ingresada por consola

Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador


se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es


alguno de lo soportados o no es la palabra "FIN". '''
print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

numero_1 = float(input('Ingrese el primero número \n'))
numero_2 = float(input('Ingrese el segundo número \n'))
operacion = str(input('Ingrese la operacion a realizar con: +,-,/,**,*  o ingrese FIN para cerrar la calculadora\n'))

suma= numero_1 + numero_2
resta= numero_1 - numero_2
division= numero_1 / numero_2
potencia= numero_1 ** numero_2
multiplicacion= numero_1 * numero_2

 
while True:
    if operacion == "+":
        print("el resultado de la suma es:",suma)

        
    elif operacion == "-":
        print("el resultado de la resta es:",resta)
        
        
    elif operacion == "/":
        print("el resultado de la division es:",division)
        
        
    elif operacion == "**": 
        print("el resultado de la potencia es:",potencia)
        
    elif operacion == "*":
        print("el resultado de la multiplicacion es:",multiplicacion)
    elif operacion =="FIN":
        print("chau")
        break
    elif operacion != "FIN" or operacion != "+"or operacion != "-" or operacion != "/" or operacion != "**" or operacion != "*":
        print("Error.Los valores validos son: +,-,**,/ y * o FIN. Pruebe de nuevo")
    
    
        
    numero_1 = float(input('Ingrese el primero número \n'))
    numero_2 = float(input('Ingrese el segundo número \n'))
    operacion = str(input('Ingrese la operacion a realizar con: +,-,/,**,*  o ingrese FIN para cerrar la caculadora\n'))