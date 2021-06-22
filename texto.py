# texto = "Shakira"

# texto[0] = "5"  NO se puede, porque string es inmutable

# del texto

# for i in texto:
#     print(i)

# print(" " in "Shakira")
# print(2 in ["a",2,3,"b"])

# print("____")
# print("    |")
# print("    |")
# print("   /_\\")

# print("____")
# print(" O  |")
# print("-   |")
# print("   /_\\")

#Ana Gabriel
# "_ _ _  _ _ _ _ _ _ _"

#arnold schwarzenegger
# "_ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _ _"

from random import choice, choices

print(choices([1,2,3,4,5,6]))

# seleccion = choice(["mango","pera","manzana","fresa"])
# print(seleccion)
frases = [] 
actores = ["arnold schwarzenegger","Al pacino","Mel gibson","Gal Gadot"]
frutas = ["mango","pera","manzana","fresa"]
deportes = ["futbol","baloncesto","ciclismo","natacion"]
frases.append(actores)
frases.append(frutas)
frases.append(deportes)
secreto = None

while True:
    opcion = input("Seleccione la categoria asi:\n1. Actores\n2. Frutas\n3. Deportes\n4. Salir\n>")

    if opcion == "1":
        secreto = choices(frases[0])[0]
        break
    
    if opcion == "2":
        secreto = choices(frases[1])[0]
        break

    if opcion == "3":
        secreto = choices(frases[2])[0]
        break

    if opcion == "4":
        break


    if " " in secreto:
        compuesto = secreto.split(" ")
        print(len(compuesto[0])*"_ "," ",len(compuesto[1])*"_ ")
    else:
        print(len(secreto)*"_ ")

while True:
    input("Ingrese la letra \n")



