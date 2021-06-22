archivo = open("prueba.txt","a+")
# archivo.write("\ndato 10")
archivo.seek(0)
numeros = archivo.readline()
numeros = numeros.split(",")

for i in numeros:
    print(int(i)**2," ")

# for i in archivo.readlines():
#     print(i)
# print(archivo.mode)
# print(archivo)