# for i in range(1,11):
#     print(i)

# i = 1
# while(i<=10):
#     print(i)
#     i = i + 1

i = -1

while(i!=4):
    print("Ingrese una opcion asi:\n1. Suma\n2. multiplicacion\n3. Iniciar sesion\n4. Salir")
    i = input(">")
    i = int(i)

    if i == 1:
        a = input("Ingrese a ")
        a = int(a)
        b = input("Ingrese b ")
        b = int(b)
        c = a + b
        print("La suma es",c)
    elif i == 2:
        a = input("Ingrese a ")
        a = int(a)
        b = input("Ingrese b ")
        b = int(b)
        c = a * b
        print("La multiplicacion es",c)
    elif i == 3:
        #TODO: Programar iniciar sesion
        pass
    elif i!=4:
        print("Opcion invalida")
    else:
        print("Hasta pronto")
    