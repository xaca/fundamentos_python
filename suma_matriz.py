def imprimir_matriz(matriz):
    for i in matriz:
        fila = i
        print("|",end="")
        for j in fila:
            if j != '':
                print(j,"",end="")
            else:
                print("  ",end="")
        print("|")
    print()

def sumar_matrices(a,b):
    c = [[0,0,0],[0,0,0],[0,0,0]]
    
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            c[i][j] = a[i][j]+b[i][j]

    return c

a = [[1,3,4],[4,2,1],[2,7,8]]
b = [[0,2,-1],[0,8,4],[3,2,1]]

imprimir_matriz(a)
imprimir_matriz(b)
imprimir_matriz(sumar_matrices(a,b))