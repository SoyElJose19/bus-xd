import csv
usuarios=[]

def compra_asientos(): #Opcion 2
    print("-----COMPRAR ASIENTOS-----")
    nombre_apellido=input("Ingrese Nombre y Apellido: ")
    edad = int(input("Ingrese su edad: "))    
    numero_telef=int(input("Ingrese Número de Teléfono: "))
    numero_asien=input("Ingrese su Asiento: ")
    monto=int(input("Monto a Cobrar por Asiento: "))
    
    if edad <18:
        descuento = monto *0.2
        total=monto-descuento
    elif edad >65:
        descuento = monto *0.15
        total=monto-descuento
    else:
         total=monto
    usuario = {
    "nombre_apellido":nombre_apellido,
    "edad":edad,
    "numero_telef":numero_telef,
    "numero_asien":numero_asien,
    "descuento":descuento,
    "total":total
    }

    usuarios.append(usuario)
    print("Asiento comprado con exitó...")   
def asientos_disponibles():#Opcion 1
        filas = 5
        colum= 4
        print ("----ASIENTOS DISPONIBLES----")
        bus =[["O" for x in range(colum)]for y in range(filas)]
        for f in range(filas):
            for c in range(colum):
                print(f'{f+1}{c+1}: [{bus[f][c]}]', end=' ')
        print()
def salida(): #Opcion salida
        print("Gracias por comprar...")
        exit()
def archivos():
    if not usuarios:
       print("No hay ventas para exportar")
       return
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    nombre_archivo = nombre_archivo.strip()
    with open (nombre_archivo,"w",newline="") as archivo:
        nombres=["nombre_apellido","edad","numero_telef","total"]
        escritor = csv.DictWriter(archivo, nombres=nombres)
        escritor.writeheader()
        for usuario in usuarios:
             escritor.writerow(usuario)