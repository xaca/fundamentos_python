# for i in range(2,21,2):
#     print(i)

# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

# i = 2
# while i<=20:
#     print(i)
#     i = i +2

#TODO: realizar un programa que calcule la suma de los numeros pares 
# desde 2 hasta n, donde n debe ser mayor a 2 y se debe pedir al usuario

# i = 2
# suma = 0

# n = input("Ingrese n ")
# n = int(n)

# while n>4 and i<=n:
#     if i%2==0:
#         suma = suma + i
#         print(suma)
#     i = i +1
# print("La suma es",suma)

menu = "Ingrese un numero:\n1.Saludar\n2.Reordenar\n3.Salir"
bandera = False

while True:
    print(menu)
    opcion = input(">")
    opcion = int(opcion)

    if opcion==1:
        print("Buenos dias")
        bandera = True

    if opcion ==2:
        menu = "Ingrese un numero:\n3.Salir\n2.Reordenar\n1.Saludar"
        bandera = True

    if opcion == 3:
        break

    if not bandera:
        print("Error, dato incorrecto")
    
    bandera = False

    # elif opcion!=1 and opcion!=2:
    #     print("Error, dato incorrecto")

    # if opcion < 1 or opcion > 3:
    #     print("Error, dato incorrecto")

# i = 0
# while i < 10:
#     j = 0
#     while j < i:
#         print("*",end="")
#         j = j + 1
#     print()
#     i = i + 1

# for i in range(1,9):
#     for j in range(i,1,-1):
#         print("*",end="")
#     print()

# while True:
#     n = input("Ingrese un numero positivo ")
#     n = int(n)

#     if n >=0:
#         print("Muy bien el numero es positivo")
#         break