import pandas

archivo = pandas.read_csv(r'C:\Users\xaca\Documents\python\productos.csv',encoding="utf8",delimiter=';')
datos = archivo.values.tolist()
cont = None
cantidad = None
valor = None
nombre = None
total = 0
for fila in datos:
    cont = 0
    for columna in fila:
        if cont==0:
            nombre = columna

        if(cont == 1):
            cantidad = int(columna)
        
        if cont==2:
            valor = int(columna)
            total = total + valor*cantidad
            print(nombre,"$",valor*cantidad,end="")
        
        cont = cont + 1
        #print(columna,end=" ")
    print()
print("--------------------")
print("Valor a pagar $",total)