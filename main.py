from classes.json import JsonUtil
from classes import Client
from classes.sorting import QuickSort,MergeSort,HeapSort,ShellSort
import sys

def creaClient():
    while True:
        empty=input("Desea agregar mas reservaciones? Si/No ").lower()
        if empty=="si":
            JsonUtil.WriteData(configData["dataPath"],Client.createClient(configData["fee"]))
        elif empty=="no":
            break     
        else:
            print("Opción no válida")

print("Gestión de reservaciones")
while True:
    hotel = input("Introduce a cual hotel quieres acceder \n\t1) Aria Ld Hotel\t2) GH Guaparo Suites\n\t3) Sunsol Ecoland\t4) Hesperia WTC  \n Opción: ").lower()
    if hotel in ("1", "aria", "aria hotel", "aria ld hotel"):
        configPath = "config/ariaConfig.json"
        break
    elif hotel in ("2", "guaparo", "guaparo suites", "gh guaparo suites"):
        configPath = "config/guaparoConfig.json"
        break
    elif hotel in ("3", "sunsol", "ecoland", "sunsol ecoland"):
        configPath = "config/sunsolConfig.json"
        break
    elif hotel in ("4", "hesperia", "hesperia wtc"):
        configPath = "config/hesperiaConfig.json"
        break
    else:
        print("Opción no válida")
print(configPath)
configData=JsonUtil.ReadData(configPath)
print(configData)
print("Accediendo a")
print(configData["hotelName"])
print(configData["address"])

content=JsonUtil.ReadData(configData["dataPath"])
if len(content)==0:
    while True:
        empty=input("No se han encontrado reservaciones, desea agregar mas reservaciones? Si/No ").lower()
        if empty=="si" or empty=="no":
            if empty in ("si"):
                data= Client.Client()
                data.createClient()
                data.__dict__
                JsonUtil.WriteData(configData["dataPath"],data)
            else:
                print("saliendo...")
                sys.exit() 
        else:
            print("Opcion no valida")
            continue
        creaClient()
        break

elif len(content)==1:
        print("Se ha cargado una reservación")  
else:
    print("Se han cargado "+str(len(content))+" reservaciones")
    #TODO Implementar condición infinita
content=JsonUtil.ReadData(configData["dataPath"])
cliente=[]
print(" Nombre   Apellido   Cédula       Email         Fecha de Reservación   Dias de estadia  Precio Total  Método de pago      ID")
for i in content:
    cliente.append(Client.Client(i["fName"],i["lName"],i["identification"],i["email"],i["reservationDate"],i["stayDays"],i["totalPrice"],i["payMethod"],i["id"]))
for i in cliente:
    print("{:^8}  {:^8}  {:^8}  {:<20}   {:<12}          {:<8}        {:<8}      {:<10}   {:<13}".format(i.fName,i.lName,i.identification,i.email,i.reservationDate,i.stayDays,i.totalPrice,i.payMethod,i.id))

