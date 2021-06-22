# TODO: Leer n y m, donde n < m, cree un numero aleatorio
# si el numero es mayor a la mitad entre n y m, imprima mayor
# en caso contrario imprima menor, si la mitad es exacta 
# imprima igual.
# - if, if-else, if-elif
# randomint
# print

from random import randint

contador = 0
x = None
n = None
m = None
aleatorio = None
mitad = None
menores = 0
mayores = 0
iguales = 0
i = 0
j = 0
k = 0

x = input("Ingrese la cantidad de veces que se ejecutara el programa ")
x = int(x)

if x > 10:
    print("Ingrese dos numeros enteros, teniendo en cuenta que n < m")
    n = input("Ingrese n ")
    m = input("Ingrese m ")

    # TODO: Validar que n y m si sean numeros, para poder ser convertidos

    n = int(n)
    m = int(m)

    while contador < x:

        if n < m:
            aleatorio = randint(n,m)
            mitad = (m+n)/2
            if aleatorio > mitad:
                mayores = mayores + aleatorio #mayor + 1
                i = i + 1
            elif aleatorio < mitad:
                menores = menores + aleatorio
                j = j + 1
            elif aleatorio == mitad:
                iguales = iguales + aleatorio
                k = k + 1
            else:
                print("El valor no es ni mayor, ni menor, ni igual")
        else:
            print("Error,",n, "no es menor a",m)
            break

        contador = contador + 1
    print("El resultado de ejecucion fue")
    print(f"Mayor {mayores}|{i} Menores {menores}|{j} Iguales {iguales}|{k}")
    
else:
    print("Error, en el valor de la x")

# TODO: Teniendo en cuenta el programa anterior, realice un ajuste donde
# se continuen calculando valores aleatorios hasta un total de x datos
# donde x se le pide al usuario, este valor debe ser mayor que 10. 
# Se van a sumar los valores menores, mayores e iguales por separado,
# y al final, se imprime el resultado obtenido.
# contadores, while, break, print-format