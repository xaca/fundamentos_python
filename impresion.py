# TODO: Leer n y m, donde n < m, cree un numero aleatorio
# si el numero es mayor a la mitad entre n y m, imprima mayor
# en caso contrario imprima menor, si la mitad es exacta 
# imprima igual.
# - if, if-else, if-elif
# randomint
# print

from random import randint

n = None
m = None
aleatorio = None
mitad = None

print("Ingrese dos numeros enteros, teniendo en cuenta que n < m")
n = input("Ingrese n ")
m = input("Ingrese m ")

# TODO: Validar que n y m si sean numeros, para poder ser convertidos

n = int(n)
m = int(m)

if n < m:
    aleatorio = randint(n,m)
    mitad = (m+n)/2
    if aleatorio > mitad:
        print("mayor")
    elif aleatorio < mitad:
        print("menor")
    elif aleatorio == mitad:
        print("igual")
    else:
        print("El valor no es ni mayor, ni menor, ni igual")
else:
    print("Error,",n, "no es menor a",m)

# TODO: Teniendo en cuenta el programa anterior, realice un ajuste donde
# se continuen calculando valores aleatorios hasta un total de x datos
# donde x se le pide al usuario, este valor debe ser mayor que 10. 
# Se van a sumar los valores menores, mayores e iguales por separado,
# y al final, se imprime el resultado obtenido.
# contadores, while, break, print-format