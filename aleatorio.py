from random import randint
# print(randint(1,5000))

for i in range(1,11):
    if randint(1,10) % 2 == 0:
        print("cara")
    else:
        print("sello")

#TODO: Crear programa que realice la tirada de una moneda 10 veces, 
#      imprima el valor final de cada ronda