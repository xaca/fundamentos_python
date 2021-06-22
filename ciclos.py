

from random import randint
tiro = None

while True:
    tiro = randint(1,6)
    if tiro==6:
        break
    if tiro%2 != 0:
        continue
    print(tiro)

print("el programa termino")
# contador = 0
# while contador<=10:
#     print(contador)
#     contador = contador + 1

# print("1. Saludar")
# print("2. Es par")
# print("3. Promedio")
# print("4. Módulo")
# print("5. Porcentaje")
# print("6. Potencia")
# print("7. Salir")