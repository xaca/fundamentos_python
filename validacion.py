palabra = "Mauricio puerta alzate perez"
# partes = palabra.split(" ")

# Crear un procedimiento para saber si una frase es palindroma,
# una frase es palindroma si se lee de izquierda a derecha y de
# derecha a izquierda de la misma forma. 
# se verlas al reves, reconocer, oso, arenera, 02022020,
# yo dono rosas, oro no doy...
# la ruta natural, ¿acaso hubo buhos aca?, dabale arroz a la zorra el abad,
# amo la pacifica paloma, nada yo soy adan, no di mi decoro cedi mi don
# anita lava la tina

# palabra = "anita lava la tina".split()
# print(palabra)
# palabra.reverse()
# print(palabra)

palabra = "anita lava la tina"
invertida = ""
i = -1

# prueba = "hola " "mundo"

while i>-(len(palabra)+1):
    if not palabra[i].isspace():
        invertida = invertida + palabra[i]
    i = i - 1

print(invertida)

palabra = palabra.replace(" ","")
# invertida = invertida.replace(" ","")

print(palabra,invertida,sep="\n")

print(palabra == invertida)

#imprimir una cadena con los siguientes formatos
# hola mundo -> odnum aloh
# hola mundo -> HoLa MuNdO
# hola mundo -> h_o_l_a M_u_n_d_o

# Crear programa que elimine las vocales de una frase

# Como se completa un caracter que pertenece a una palabra,
# dejando el espacio para los demas caracteres

# for i in partes:
#     print(i.capitalize()," ",end="")

# for i in palabra:
#     print(i,i.isspace())

# print(palabra.swapcase())

# numero = input("Ingrese un numero ")

# print(len(numero))
# print(numero.isdigit())
# print(numero.isnumeric())

# if numero.isnumeric() or numero.isdecimal():
#     numero = float(numero)
#     print(numero**2)
# else:
#     print("Error de lectura de datos")