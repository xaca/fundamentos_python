# Realizar la siguiente conversion, teniendo en cuenta cada palabra
# de la frase, donde los indices pares van en mayuscula y los impares en minuscula
# hola mundo -> HoLa MuNdO

frase = "Mision TIC 2021 Estudiantes Exitosos"
frase = frase.lower()
palabras = frase.split(" ")
cont = 0
respuesta = ""
letra = None
palabra = None

for i in palabras:
    cont = 0
    palabra = i

    while cont < len(palabra):
        letra = palabra[cont]
        if cont % 2 == 0:
            respuesta = respuesta + letra.upper()
        else:
            respuesta = respuesta + letra
        cont = cont + 1
    
    print(respuesta,end=" ")
    respuesta = ""
print()
# cheat sheet
