'''
# 1) Desarrollar una función que reciba tres números positivos y devuelva el mayor de los 
# tres, sólo si éste es único(mayor estricto). En caso de no existir el mayor estricto 
# devolver - 1. No utilizar operadores lógicos ( and , or , not). Desarrollar también un
# programa para ingresar los tres valores, invocar a la función y mostrar el máximo 
# hallado, o un mensaje informativo si éste no existe.
<<<<<<< HEAD

#función
def hayarMayor(num1,num2,num3):

    return max

# programa principal
num1= int(input("Ingrese el primer número"))
num2= int(input("Ingrese el segundo número"))
num3= int(input("Ingrese el tercer número"))
maximo= hayarMayor(num1,num2,num3)
print("El numero mayor es {}").format(maximo)
=======
 
# funcion
def mayor_estricto(num1, num2, num3):
    """
    Función que recibe tres números positivos y devuelve el mayor de los tres, 
    sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto, 
    devuelve -1. No utiliza operadores lógicos (and, or, not).
    """
    mayor = -1  # Inicializar el mayor como -1
    if num1 > num2:
        if num1 > num3:
            mayor = num1
    elif num2 > num1:
        if num2 > num3:
            mayor = num2
    if mayor != -1:  # Si se encontró un mayor estricto, verificar que sea único
        if mayor == num1 and mayor != num2 and mayor != num3:
            return mayor
        elif mayor == num2 and mayor != num1 and mayor != num3:
            return mayor
        elif mayor == num3 and mayor != num1 and mayor != num2:
            return mayor
    return -1  # No se encontró un mayor estricto


#programa principal

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

maximo = mayor_estricto(num1, num2, num3)

if maximo == -1:
    print("No existe un mayor estricto entre los tres números ingresados.")
else:
    print(f"El mayor estricto entre {num1}, {num2} y {num3} es: {maximo}")



# 2) Desarrollar una función que reciba tres números enteros positivos y verifique si corresponden 
# a una fecha válida (día, mes, año). Devolver True o False según la fecha sea correcta o no. 
# Realizar también un programa para verificar el comportamiento de la función.

# función
def mayor_estricto(num1, num2, num3):
    """
    Función que recibe tres números positivos y devuelve el mayor de los tres, 
    sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto, 
    devuelve -1. No utiliza operadores lógicos (and, or, not).
    """
    mayor = -1  # Inicializar el mayor como -1
    if num1 > num2:
        if num1 > num3:
            mayor = num1
    elif num2 > num1:
        if num2 > num3:
            mayor = num2
    if mayor != -1:  # Si se encontró un mayor estricto, verificar que sea único
        if mayor == num1 and mayor != num2 and mayor != num3:
            return mayor
        elif mayor == num2 and mayor != num1 and mayor != num3:
            return mayor
        elif mayor == num3 and mayor != num1 and mayor != num2:
            return mayor
    return -1  # No se encontró un mayor estricto

# programa principal
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

maximo = mayor_estricto(num1, num2, num3)

if maximo == -1:
    print("No existe un mayor estricto entre los tres números ingresados.")
else:
    print(f"El mayor estricto entre {num1}, {num2} y {num3} es: {maximo}")

'''
