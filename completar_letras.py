from random import choice

frases = [] 
actores = ["schwarzenegger","pacino","gibson","Gadot"]
frutas = ["mango","pera","manzana","fresa"]
deportes = ["futbol","baloncesto","ciclismo","natacion"]
frases.append(actores)
frases.append(frutas)
frases.append(deportes)

#TODO:Este programa solo funciona con una palabra, falta ajustarlo para que funcione con frases
secreto = None #"Cafe Tacuba" #"Metallica"
progreso = None
letra = None
temp = None
cont = 0
bandera = False
puntos_pc = 0
puntos_humano = 0
intentos = 0

while True:

    opcion = input("Seleccione la categoria asi:\n1. Actores\n2. Frutas\n3. Deportes\n4. Salir\n>")
    
    if opcion == "1":
        bandera = True
        secreto = choice(frases[0])

    if opcion == "2":
        bandera = True
        secreto = choice(frases[1])

    if opcion == "3":
        bandera = True
        secreto = choice(frases[2])

    if opcion == "4":
        break

    if bandera:
        secreto = secreto.lower()
        progreso = (len(secreto)*"_ ").split()

        while True:
            letra = input("Ingrese una letra ")
            # TODO: Validar el error si se ingresa un numero
            # TODO: Evitar el ingreso de letras repetidas, use "a" in ["a","e"] esto da True
            if len(letra)==1:
                if secreto.find(letra)!=-1:
                    temp = ""
                    cont = 0

                    for i in secreto:
                        if i == letra:
                            progreso[cont] = i
                        cont += 1
                    print(" ".join(progreso))

                    if "".join(progreso) == secreto:
                        print("¡Gano!")
                        puntos_humano = puntos_humano + 1
                        break
                else:
                    intentos = intentos + 1
                    if intentos == 7:
                        print("Perdio")
                        puntos_pc = puntos_pc + 1
                        break
                    
                    # TODO:Mostrar el avance del pesonaje ahorcandose

                    print("Mostrar error")
            else:
                print("Letra no valida")

    intentos = 0
    print("El puntaje es","\nHumano",puntos_humano,"\nComputador",puntos_pc)