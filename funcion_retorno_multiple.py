def prueba():
    return True,4,"marcador"

x,y,z = prueba()

# print(x,y,z)

# puntaje = 0
# texto = "mensaje"

# def cambiar_valor(nuevo_puntaje): 
#     global texto
#     texto = nuevo_puntaje
#     print(texto)

# # print(puntaje)
# cambiar_valor(80)
# # print(puntaje)
# print(texto)

puntos_humano = 0
puntos_pc = 0

def juego(bandera):
    global puntos_humano
    global puntos_pc
    # puntos_pc = 0
    # puntos_humano = 0

    if bandera:
        puntos_pc = puntos_pc + 1
    else:
        puntos_humano = puntos_humano + 1

# print(puntos_humano,puntos_pc)
# juego(True)
# print(puntos_humano,puntos_pc)
# juego(True)
# print(puntos_humano,puntos_pc)
# juego(False)
# print(puntos_humano,puntos_pc)

print("  ____")
print("  O   |")
print(" -|-  |")
print("  /\\  |")
print("     /_\\")