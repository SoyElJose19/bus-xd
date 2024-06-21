import time,os
from funciones import *
while True:
    os.system('cls')
    print ("MENÚ COMPRAS")
    print ("1.- Mostrar Asientos Disponibles")
    print ("2.- Comprar Asientos")
    print ("3.- Mostrar la venta realizada")
    print ("4.- Generar comprobante de compras")
    print ("5.- Salir")
    opc = int(input("Elija su opción: "))
    os.system("cls")
    if opc==1:
        asientos_disponibles()
    elif opc==2:
        compra_asientos()
    elif opc==3:
        pass    
    elif opc==4:
        archivos()
    else:
        salida()
    time.sleep(3)