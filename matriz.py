triqui = list()
triqui.append(['X','',''])
triqui.append(['','X',''])
triqui.append(['','','O'])

# print(triqui[0])
# triqui[0] = ['X','O','']
# print(triqui[0])
triqui[2][0]='O'
triqui[0][2]='X'

for i in triqui:
    fila = i
    print("|",end="")
    for j in fila:
        if j != '':
            print(j,end="")
        else:
            print("  ",end="")
    print("|")

# | X O  |
# |   X  |
# | O    |