opcion = None

def leerNumero(mensaje):
    n = input(mensaje)
    return int(n)

def prueba():
    print("Hola, soy una funcion")

def sumar():
    x = leerNumero("Ingrese x ")
    y = leerNumero("Ingrese y ")
    return x + y

def restar():
    x = leerNumero("Ingrese x ")
    y = leerNumero("Ingrese y ")
    return x - y

def suma(x,y):
    return x + y

def resta(x,y):
    return x - y

def saludar(nombre="Ana"):
    print(f"Hola {nombre}")

def proceso():
    return "Hola Tengo un retorno"

def imprimir_menu():
    print("1. Sumar\n2. Restar\n3. Salir")

while True:
    imprimir_menu()
    opcion = leerNumero("Ingrese una opcion ")

    if opcion == 1:
        sumar()
    elif opcion == 2:
        restar()
    elif opcion == 3:
        break
    else:
        print("Error valor incorrecto")


# print(proceso())
#prueba()
# saludar()
# saludar("Yeison")
# print(suma(34,12))
# print(suma(3,5))

# TODO: Realizar un menu con las siguientes opciones:
# suma, resta, multiplicacion, division, residuo
# por medio de funciones, realizar las operaciones 
# y luego imprimir el resultado.
