# hola mundo feliz -> h_o_l_a M_u_n_d_o f_e_l_i_z

# frase = "hola mundo"
# respuesta = ""
# cont = 0
# for i in frase:
#     respuesta = respuesta + i
#     if cont %2 == 0:
#         respuesta = respuesta + "_"
#     # print(i,sep="_",end="")
#     cont = cont + 1
# print(respuesta)

# print("a","b","c",sep="_")

# palabra = "muercielago"
# respuesta = ""
# for i in palabra:
#     if i!="a" and i!="e" and i!="i" and i!="o" and i!="u":
#         respuesta = respuesta + i
# print(respuesta)
# precios = [2200,1500,23000,5000,4500,1000,20000]
# for i in precios:
#     print(f"${i}")

# Cree una tabla con los nombres de los productos,que estan en una lista
# la primera posicion son los nombres de los productos y la segunda los precios 
# como se muestra a continuacion

# X Forma incorrecta
# | Nombre producto |  Precio |
# | Camiseta        | $ 35000 |
# | Medias        | $ 5000 |
# | tenis        | $ 235000 |
# | maleta        | $ 55000 |

# Forma correcta
# | Nombre producto |  Precio |
# -----------------------------
# |        Camiseta | $ 35000 |
# |          Medias | $ 5000  |
# |           Tenis | $ 235000|
# |          Maleta | $ 55000 |
# -----------------------------
# |          Total  | $ 330000|

# precios = [2200,1500,23000]
# productos = ["camiseta","Tenis","MORRAL"]
# datos = list()
# datos.append(productos)
# datos.append(precios)
# for i in precios:
#     print("|${:>5}|".format(i))