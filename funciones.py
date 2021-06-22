def suma():
    x = input("Ingrese x ")
    y = input("Ingrese y ")
    z = None
    if x.isnumeric() and y.isnumeric():
        z = float(x) + float(y)
    return z

def potencia(x,y,z):
    x = x**x
    y = y**y
    z = z**z
    return x,y,z

nombre = "Juan"

def prueba(nombre="Hannah"):
    return nombre

nombre = prueba("Matias")
print(nombre)
# resultado = potencia(2,3,4)
# print(resultado[0])

# resultado = suma()
# print(resultado)