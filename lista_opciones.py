opciones = list()
opciones.append("1.Suma")
opciones.append("2.Resta")
opciones.append("3.Multiplicacion")
opciones.append("4.Division")
opciones.append("5.Salir")

# temp = opciones[2]
# opciones[2] = opciones[0]
# opciones[0] = temp
bandera = False

while True:
    for i in opciones:
        print(i)

    opcion = input(">")
    
    if opcion == "1":
        bandera = True
        print("Sumar")

    if opcion == "2":
        bandera = True
        print("Resta")

    if opcion == "3":
        bandera = True
        print("Multiplicar")

    if opcion == "4":
        bandera = True
        print("Division")
    
    if opcion == "5":
        bandera = True
        break

    if not bandera:
        print("Error dato incorrecto")
    
    bandera = False