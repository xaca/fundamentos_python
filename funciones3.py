def cantidad_jugadas(matriz):
    total = 0
    for i in matriz:
        fila = i
        for j in fila:
            if(j!=""):
                total = total + 1
    
    return total

def imprimir_matriz(matriz):
    for i in matriz:
        fila = i
        print("|",end="")
        for j in fila:
            if j != '':
                print(j,end="")
            else:
                print("  ",end="")
        print("|")

def actualizar_jugada(matriz,fila,col,caracter):
    matriz[fila][col] = caracter

triqui = list()
triqui.append(['','','']) 
triqui.append(['','','']) 
triqui.append(['','','']) 

print(cantidad_jugadas(triqui))
actualizar_jugada(triqui,0,0,"X")
actualizar_jugada(triqui,1,0,"X")
imprimir_matriz(triqui)
print(cantidad_jugadas(triqui))
actualizar_jugada(triqui,2,2,"O")
print(cantidad_jugadas(triqui))
imprimir_matriz(triqui)

# Crear una funcion, que asigne una jugada aleatoria