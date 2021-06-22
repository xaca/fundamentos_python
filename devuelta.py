total = 200000
pago = input("Ingrese el pago ")
pago = float(pago)

if pago == total:
    print("Gracias por su compra")
elif pago > total:
    print("Su devuelta es ",pago-total)
    print("Gracias por su compra")
else:
    print("Fondos insuficientes")


# if pago == total:
#     print("Gracias por su compra")
# else:
#     if pago > total:
#         print("Su devuelta es ",pago-total)
#         print("Gracias por su compra")
#     else:
#         print("Fondos insuficientes")