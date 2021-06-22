from random import choice

#TODO:Este programa solo funciona con una palabra, falta ajustarlo para que funcione con frases
frases = [] 
secreto = None #"Cafe Tacuba" #"Metallica"
progreso = None
bandera = False
puntos_pc = 0
puntos_humano = 0
intentos = 0

def inicializar_palabras():
    global frases
    actores = ["schwarzenegger","pacino","gibson","Gadot"]
    frutas = ["mango","pera","manzana","fresa"]
    deportes = ["futbol","baloncesto","ciclismo","natacion"]
    paises = ["colombia","peru","ecuador"]
    generos = ["rock","salsa","merengue","cumbia","metal","reggae"]
    frases.append(actores)
    frases.append(frutas)
    frases.append(deportes)
    frases.append(paises)
    frases.append(generos)

def imprimir_error(numero):
    # TODO: El personaje no se ahorca graficamente, arreglarlo
    if numero == 1:
        print("____")
        print(" O  |")
        print("    |")
        print("   /_\\")
    elif numero == 2:
        print("  ____")
        print("  O   |")
        print(" -    |")
        print("     /_\\")
    elif numero == 3:
        print("  ____")
        print("  O   |")
        print(" -|   |")
        print("     /_\\")
    elif numero == 4:
        print("  ____")
        print("  O   |")
        print(" -|-  |")
        print("     /_\\")
    elif numero == 5:
        print("  ____")
        print("  O   |")
        print(" -|-  |")
        print("  /   /_\\")
    elif numero == 6:
        print("  ____")
        print("  O   |")
        print(" -|-  |")
        print("  /\\   /_\\")

def palabra_aleatoria(numero):
    return True,choice(frases[numero])

def juego(bandera):
    global secreto
    global puntos_pc
    global puntos_humano
    global progreso
    global intentos
    letra = None
    temp = None
    cont = 0

    if bandera:
        secreto = secreto.lower()
        progreso = (len(secreto)*"_ ").split()

    while True:
        letra = input("Ingrese una letra ")
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
                if intentos == 6:
                    print("Perdio")
                    puntos_pc = puntos_pc + 1
                    break
                else:
                    imprimir_error(intentos)
        else:
            print("Letra no valida") 

    intentos = 0

def imprimir_puntaje():
    global puntos_humano,puntos_pc
    print("El puntaje es","\nHumano",puntos_humano,"\nComputador",puntos_pc)

inicializar_palabras()

while True:

    opcion = input("Seleccione la categoria asi:\n1. Actores\n2. Frutas\n3. Deportes\n4. Paises\n5. Generos musicales \n6. Salir\n>")
    
    if opcion == "1":
        bandera,secreto = palabra_aleatoria(0)

    if opcion == "2":
        bandera,secreto = palabra_aleatoria(1)

    if opcion == "3":
        bandera,secreto = palabra_aleatoria(2)
    
    if opcion == "4":
        bandera,secreto = palabra_aleatoria(3)

    if opcion == "5":
        bandera,secreto = palabra_aleatoria(4)

    if opcion == "6":
        break
  
    juego(bandera)
    imprimir_puntaje()

    input("Presione enter para continuar")