expresion = input("Ingrese un booleano ")
print(type(expresion))
expresion = not(expresion == "False")
print(expresion == False)
print(type(expresion))
print(3 if expresion else 8)
