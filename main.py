import re
from classes.json import JsonUtil
from classes import Client
from classes.sorting import QuickSort,MergeSort,HeapSort,ShellSort
import sys
#Marco Vilera
#29779102
#Algoritmos y Estructuras II
#305C1

def creaClient(path,fee):
    #Crea cuantos clientes el usuario desee, utilizando el método .createClient() de la clase Client
    #path=ruta del archivo .json donde se guardarán los objetos clase Client
    #fee: Tarifa de coste del hoepedaje por dia
    while True:
        empty=input("Desea agregar más reservaciones? Si/No ").lower()
        if empty=="si":
            data= Client.Client()
            data.createClient(fee)
            data.__dict__
            JsonUtil.WriteData(path,data)
            continue
        elif empty=="no":
            break     
        else:
            print("Opción no válida")

def printTable(arr):
    #Imprime en consola en formato tabular el contenido del arreglo de objetos Client
    #arr= Arreglo de objetos Clients
    print(" Nombre   Apellido   Cédula       Email                  Fecha de Reservación   Días de estadía  Precio Total    Método de pago       ID")
    for i in arr:
        print("{:^8}  {:^8}  {:^8}  {:<30}   {:<12}           {:<8}        {:<9}      {:<10}   {:<13}".format(i.fName,i.lName,i.identification,i.email,i.reservationDate,i.stayDays,i.totalPrice,i.payMethod,i.id))

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

#Lectura del archivo de configuración
configData=JsonUtil.ReadData(configPath)

#Orden prederminado del archivo de configuración(Ascendente/Descendente)
order=configData["order"]

DATAPATH=configData["dataPath"]
FEE=configData["fee"]
print("Accediendo a")
print(configData["hotelName"])
print(configData["address"])

#Se carga en la variable un arreglo de diccionarios
content=JsonUtil.ReadData(DATAPATH)

if len(content)==0:
    #En caso de que el archivo esté vacio
    while True:
        empty=input("No se han encontrado reservaciones, desea agregar más reservaciones? Si/No ").lower()
        if empty=="si" or empty=="no":
            if empty in ("si"):
                #Se crea un objeto Client
                data = Client.Client()
                #Se llena el objeto
                data.createClient(FEE)
                #Se usa el atributo heredado __dict__ para convertir el objeto en un diccionario
                data.__dict__
                #Se carga en el archivo .json
                JsonUtil.WriteData(DATAPATH,data)
            else:
                print("Saliendo...")
                sys.exit() 
        else:
            print("Opcion no valida")
            continue
        creaClient(DATAPATH,FEE)
        break

elif len(content)==1:
        print("Se ha cargado una reservación")
        creaClient(DATAPATH,FEE)  
else:
    print("Se han cargado "+str(len(content))+" reservaciones")
    creaClient(DATAPATH,FEE)
content=JsonUtil.ReadData(DATAPATH)
cliente=[]
print("Cargando reservaciones...")

#Se lee la lista de diccionarios y se crea cada objeto con cada clave
for i in content:
    #Lista de Objetos Client
    cliente.append(Client.Client(i["fName"],i["lName"],i["identification"],i["email"],i["reservationDate"],i["stayDays"],i["totalPrice"],i["payMethod"],i["id"]))

printTable(cliente)
while True:
    #Bucle principal
    menu=input("Que desea realizar? \n\t1) Búsqueda por criterios \t2) Búsqueda por rango de fechas \t3) Listar usando ShellSort\n\t4) Listar usando HeapSort  5) Opciones\t6) Salir\n Opción: ").lower()
    if menu in ("1","busqueda por criterios","búsqueda por criterios"):
        while True:
            #Lista de objetos con la que se usará el algoritmo QuickSort
            clienteQ=cliente
            crit=input("Que desea realizar? \n\t1) Búsqueda por un criterio\t2) Búsqueda por multiples criterios\t3) Retroceder\nOpción: ").lower()
            
            #Busqueda por un solo criterio
            if crit in ("1","búsqueda por un criterio","busqueda por un criterio"):
               while True:
                   atr=input("Introduce el criterio a buscar \n\t1) Nombre \t2) Apellido \t3) Cédula \t4) Email  \t5) Fecha de reservación \n\t6) Días de estadía \t7)Precio Total \t8) Método de pago \t9) Id \nOpción: ").lower()
                   #Validación de que el criterio sea válido
                   if atr in ("1","nombre","2","apellido","3","cédula","cedula",
                              "4","email","5","fecha de reservación","fecha de reservacion",
                              "6","días de estadía","días de estadia","dias de estadía","dias de estadia","7","precio total",
                              "8","método de pago","metodo de pago","9","id"):
                       if atr in ("1","nombre"):
                           clienteQ=QuickSort.quicksort(0,len(clienteQ)-1,clienteQ,order,"fName")
                           printTable(clienteQ)
                           break
                       elif atr in ("2","apellido"):
                           clienteQ=QuickSort.quicksort(0,len(clienteQ)-1,clienteQ,order,"lName")
                           printTable(clienteQ)
                           break
                       elif atr in ("3","cédula","cedula"):
                           clienteQ=QuickSort.quicksort(0,len(clienteQ)-1,clienteQ,order,"identification")
                           printTable(clienteQ)
                           break
                       elif atr in ("4","email"):
                           clienteQ=QuickSort.quicksort(0,len(clienteQ)-1,clienteQ,order,"email")
                           printTable(clienteQ)
                           break
                       elif atr in ("5","fecha de reservación","fecha de reservacion"):
                           clienteQ=QuickSort.quicksort(0,len(clienteQ)-1,clienteQ,order,"reservationDate")
                           printTable(clienteQ)
                           break
                       elif atr in ("6","días de estadía","días de estadia","dias de estadía","dias de estadia"):
                           clienteQ=QuickSort.quicksort(0,len(clienteQ)-1,clienteQ,order,"stayDays")
                           printTable(clienteQ)
                           break
                       elif atr in ("7","precio total"):
                           clienteQ=QuickSort.quicksort(0,len(clienteQ)-1,clienteQ,order,"totalPrice")
                           printTable(clienteQ)
                           break
                       elif atr in ("8","método de pago","metodo de pago"):
                           clienteQ=QuickSort.quicksort(0,len(clienteQ)-1,clienteQ,order,"payMethod")
                           printTable(clienteQ)
                           break
                       elif atr in ("9","id"):
                           clienteQ=QuickSort.quicksort(0,len(clienteQ)-1,clienteQ,order,"id")
                           printTable(clienteQ)
                           break
                    #En caso de no serlo, se pedirá un criterio válido
                   else:
                       print("Criterio no válido")
                       continue
                   break
               
            #Busqueda por varios criterios
            elif crit in ("2","búsqueda por multiples criterios","busqueda por multiples criterios"):
                while True:
                    atr1=input("Introduce el primer atributo a buscar \n\t1) Nombre \t2) Apellido \t3) Cédula \t4) Email  \t5) Fecha de reservación \n\t6) Días de estadía \t7)Precio Total \t8) Método de pago \t9) Id \nOpción: ").lower()
                    atr2=input("Introduce el segundo atributo a buscar \n\t1) Nombre \t2) Apellido \t3) Cédula \t4) Email  \t5) Fecha de reservación \n\t6) Días de estadía \t7)Precio Total \t8) Método de pago \t9) Id \nOpción: ").lower()
                    #Validación de que los atributos sean válidos
                    if atr1 in ("1","nombre","2","apellido","3","cédula","cedula",
                              "4","email","5","fecha de reservación","fecha de reservacion",
                              "6","días de estadía","días de estadia","dias de estadía","dias de estadia","7","precio total",
                              "8","método de pago","metodo de pago","9","id") and atr2 in ("1","nombre","2","apellido","3","cédula","cedula",
                              "4","email","5","fecha de reservación","fecha de reservacion",
                              "6","días de estadía","días de estadia","dias de estadía","dias de estadia","7","precio total",
                              "8","método de pago","metodo de pago","9","id"):
                            
                            #Atributo 1
                            if atr1 in ("1","nombre"):
                                atr1="fName"
                                
                            elif atr1 in ("2","apellido"):
                                atr1="lName"
                                
                            elif atr1 in ("3","cédula","cedula"):
                                atr1="identification"
                                
                            elif atr1 in ("4","email"):
                                atr1="email"
                                
                            elif atr1 in ("5","fecha de reservación","fecha de reservacion"):
                                atr1="reservationDate"
                                 
                            elif atr1 in ("6","días de estadía","días de estadia","dias de estadía","dias de estadia"):
                                atr1="stayDays"
                                
                            elif atr1 in ("7","precio total"):
                                atr1="totalPrice"
                                
                            elif atr1 in ("8","método de pago","metodo de pago"):
                                atr1="payMethod"
                                    
                            elif atr1 in ("9","id"):
                                atr1="id"
                            
                            #Atributo 2
                            if atr2 in ("1","nombre"):
                                atr2="fName"
                                
                            elif atr2 in ("2","apellido"):
                                atr2="lName"
                                
                            elif atr2 in ("3","cédula","cedula"):
                                atr2="identification"
                                
                            elif atr2 in ("4","email"):
                                atr2="email"
                                     
                            elif atr2 in ("5","fecha de reservación","fecha de reservacion"):
                                atr2="reservationDate"
                                    
                            elif atr2 in ("6","días de estadía","días de estadia","dias de estadía","dias de estadia"):
                                atr2="stayDays"
                                                      
                            elif atr2 in ("7","precio total"):
                                atr2="totalPrice" 
                                
                            elif atr2 in ("8","método de pago","metodo de pago"):
                                atr2="payMethod"
                                
                            elif atr2 in ("9","id"):
                                atr2="id"

                            clienteQ=QuickSort.quicksort(0,len(clienteQ)-1,clienteQ,configData["order"],atr1,atr2)
                            printTable(clienteQ)   
                            break
                    else:
                        #En caso de que alguno no sea válido, se volverá al principio del bucle
                        print("Opción no válida")
                        continue
            #Salida al bucle principal
            elif crit in ("3","retroceder"):
                break
            else:
                print("Opción no valida")
                continue

    #Búsqueda por fechas
    elif menu in ("2","busqueda por rango de fechas","búsqueda por rango de fechas"):
        while True:
            clienteM=cliente
            date1 = input("Introduce la primera fecha en el siguiente formato dd/mm/aaaa: ")
            date2 = input("Introduce la segunda fecha en el siguiente formato dd/mm/aaaa: ")
            #Se válida que las fechas cumplan con el formato dd/mm/yyyy
            if not re.search(r"^([0-3]{1}[0-9]{1})/([0-1]{1}[0-9]{1})/([0-9]{4})$", date1):
                print("La primera fecha no es válida.")
                continue

            if not re.search(r"^([0-3]{1}[0-9]{1})/([0-1]{1}[0-9]{1})/([0-9]{4})$", date2):
                print("La segunda fecha no es válida.")
                continue
            #Se convierten los dias, meses y años en cadenas independientes
            day1, month1, year1 = date1.split("/")
            day2, month2, year2 = date2.split("/")


            
            #Se valida que los meses sean válidos
            if month1 not in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
                print("El mes de la primera fecha no es válido.")
                continue
            elif month2 not in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
                print("El mes de la segunda fecha no es válido.")
                continue

            #En función del mes, se válida si el día es valido

            #En caso de que el año sea biciesto
            if month1 == "02":
                if int(year1) % 4 == 0 and int(year1) % 100 != 0 or int(year1) % 400 == 0:
                    if int(day1) > 29:
                        print("El día de la primera fecha no es válido.")
                        continue
                else:
                    if int(day1) > 28:
                        print("El día de la primera fecha no es válido.")
                        continue

            if month2 == "02":
                if int(year2) % 4 == 0 and int(year2) % 100 != 0 or int(year2) % 400 == 0:
                    if int(day2) > 29:
                        print("El día de la segunda fecha no es válido.")
                        continue
                else:
                    if int(day2) > 28:
                        print("El día de la segunda fecha no es válido.")
                        continue    

            if month1 in ["01", "03", "05", "07", "08", "10", "12"]:
                if int(day1) > 31:
                    print("El día de la primera fecha no es válido.")
                    continue

            elif month2 in ["01", "03", "05", "07", "08", "10", "12"]:
                if int(day2) > 31:
                    print("El día de la segunda fecha no es válido.")
                    continue
            else:
                if int(day1) > 30:
                    print("El día de la primera fecha no es válido.")
                    continue
                if int(day2) > 30:
                    print("El día de la segunda fecha no es válido.")
                    continue

            #Se comprueba que el año inicial no sea mayor que el final
            if int(year1) > int(year2):
                print("La primera fecha debe ser anterior o igual a la segunda fecha.")
                continue
            #En caso que sea mismo año, se válida los dias y meses
            elif int(year1) == int(year2):
                if int(month1) > int(month2):
                    print("La primera fecha debe ser anterior o igual a la segunda fecha.")
                    continue
                elif int(month1) == int(month2):
                    if int(day1) > int(day2):
                        print("La primera fecha debe ser anterior o igual a la segunda fecha.")
                        continue
            #Primero se eliminan los meses que no estén en el intervalo
            clienteM=MergeSort.dateFilter(cliente,date1,date2)
            clienteM=MergeSort.merge_sort(clienteM,order)
            printTable(clienteM)
            break
    
    #Listar usando Shellsort
    elif menu in ("3","listar usando shellsort"):
        #Lista de objetos Client que se usará para el algoritmo Shellsort 
        while True:
            clienteS=cliente
            atr=input("Introduce el criterio a buscar \n\t1) Nombre \t2) Apellido \t3) Cédula \t4) Email  \t5) Fecha de reservación \n\t6) Días de estadía \t7)Precio Total \t8) Método de pago \t9) Id \nOpción: ").lower()
                   #Validación de que el criterio sea válido
            if atr in ("1","nombre","2","apellido","3","cédula","cedula",
                              "4","email","5","fecha de reservación","fecha de reservacion",
                              "6","días de estadía","días de estadia","dias de estadía","dias de estadia","7","precio total",
                              "8","método de pago","metodo de pago","9","id"):
                
                if atr in ("1","nombre"):
                    ShellSort.shellSort(clienteS,len(clienteS),order,"fName")

                elif atr in ("2","apellido"):
                    ShellSort.shellSort(clienteS,len(clienteS),order,"lName")

                elif atr in ("3","cédula","cedula"):
                    ShellSort.shellSort(clienteS,len(clienteS),order,"email")

                elif atr in ("4","email"):
                    ShellSort.shellSort(clienteS,len(clienteS),order,"identification")

                elif atr in ("5","fecha de reservación","fecha de reservacion"):
                    ShellSort.shellSort(clienteS,len(clienteS),order,"reservationDate")

                elif atr in ("6","días de estadía","días de estadia","dias de estadía","dias de estadia"):
                    ShellSort.shellSort(clienteS,len(clienteS),order,"stayDays")

                elif atr in ("7","precio total"):
                    ShellSort.shellSort(clienteS,len(clienteS),order,"totalPrice")

                elif atr in ("8","método de pago","metodo de pago"):
                    ShellSort.shellSort(clienteS,len(clienteS),order,"payMethod")

                elif atr in ("9","id"):
                    ShellSort.shellSort(clienteS,len(clienteS),order,"id")
                    
                    #En caso de no serlo, se pedirá un criterio válido
            else:
                print("Criterio no válido")
                continue
            printTable(clienteS)
            break
       
        
    
    #Listar usando HeapSort en función de los dias de estadía
    elif menu in ("4","listar usando heapsort"):
        #Lista de objetos Client que se usará para el algoritmo HeapSort 
        clienteH=cliente
        HeapSort.heapSort(clienteH,order)
        printTable(clienteH)
    
    #Opciones para cambiar el orden de muestra(Ascendente/Descendente)
    elif menu in ("5","opciones"):
        if order=="asc":
            print("Orden predeterminado: Ascendente")
        else:
            print("Orden predeterminado: Descendente") 
        cOrder=input("Desea cambiar el orden predeterminado? Si/No ").lower()
        while True:
            #Se valida que cOrder sea válido
            if cOrder=="si":
                if order=="asc":
                    order="desc"
                    print("Cambiando a Descendente...")
                else:
                    order="asc"
                    print("Cambiando a Ascendente...")
                break
            elif cOrder=="no":
                print("Retrocediendo...")
                break
            else:
            #Si no, devolverá al principio del bucle
                print("Opción no válida")
                continue

    elif menu in("6","salir"):
        #Sálida del programa
        print("Saliendo...")
        break
    else:
        #En caso de no ser una opción válida, se volverá al principio del bucle
        print("Opción no valida")
        continue         
