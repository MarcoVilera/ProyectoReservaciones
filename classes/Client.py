import re

#TODO Documentar codigo
class Client:
    #Objeto Cliente: Alberga toda la información de cada cliente para luego acceder a ella
    #fName = Nombre del cliente
    #lName = Apellido del cliente
    #identification = Cédula del cliente
    #email = Email del cliente
    #reservationDate = Fecha de reservación
    #stayDays = días de estadía
    #totalPrice = Precio total
    #payMethod = Método de pago, generado automaticamente.
    #id = Identificador de cada reservación, generado automaticamente.
    def __init__(self,fName="",lName="",identification="",email="",reservationDate="",stayDays=0,totalPrice=0,payMethod="",id=""):
        self.fName=fName
        self.lName=lName
        self.identification=identification
        self.email=email
        self.reservationDate=reservationDate
        self.stayDays=stayDays
        self.totalPrice=totalPrice
        self.payMethod=payMethod
        self.id=id
        

    def createClient(self,fee):
       #Método que rellena toda la información del cliente
       #fee = Tarifa del coste del día, se usa para calcular el coste total 
        print("Introducir datos del cliente")

        #Nombre y Apellido
        while True:
            #Se valida que el nombre solo contenga carácteres alfanumericos
            cName=input("Introduce el nombre del cliente ")
            cLastN=input("Introduce el apellido del cliente ")
            if re.search(r"[^a-zA-ZñÑáéíóúÁÉÍÓÚ\s]", cName):
                print("El nombre no puede contener números o caracteres especiales")
                continue 
            #Se valida que el apellido solo contenga carácteres alfanumericos
            elif re.search(r"[^a-zA-ZñÑáéíóúÁÉÍÓÚ\s]", cLastN):
                print("El apellido no puede contener números o caracteres especiales") 
                continue
            else:
                self.fName=cName.capitalize()
                self.lName=cLastN.capitalize()
                 
                break

        #Cédula     
        while True:
            cIdentification = input("Introduce la cédula del cliente ")
            #Si se ingresa algún como separador, se eliminará
            cIdentification = cIdentification.replace(".", "")

            #Se valida que la cédula sea válida
            if re.search(r"^([0-9]{6,8})$", cIdentification):
                self.identification=cIdentification
                 
                break
            elif len(cIdentification)<=5 or len(cIdentification)>=9:
                print("La cédula debe tener al menos 6 digitos y máximo 8")
            else:
                print("La cédula no puede contener caracteres especiales o alfanumericos")
        
        #Email
        while True:
            cEmail=input("Introduce el correo electronico del cliente ")
            #Se valida que el correo tenga estructura de un correo electronico ej: cadenaTexto@correo.com
            if re.search(r"^[a-zA-Z0-9][a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$", cEmail):
                self.email=cEmail
                 
                break
            else:
                print("Correo electronico no válido")

        #Fecha de Reservación
        while True:
            cReservationDate = input("Introduce la fecha de reservación del cliente en el siguiente formato dd/mm/aaaa: ")
            #Se valida que la fecha sea válida
            if not re.search(r"^([0-3]{1}[0-9]{1})/([0-1]{1}[0-9]{1})/([0-9]{4})$", cReservationDate):
                print("Fecha no válida.")
                continue
            #Se divide el día, mes y año en cadenas independientes
            day, month, year = cReservationDate.split("/")

            #Se evalua si el mes y sus días son válidos
            if month in ["01", "03", "05", "07", "08", "10", "12"]:
                if int(day) > 31:
                    print("Fecha no válida.")
                    continue
            elif int(month)>12 or int(month)<1:
                print("Fecha no válida.")

            #Año bisciesto o no y comprobar si los días son válidos
            elif month == "02":
                if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
                    if int(day) > 29:
                        print("Fecha no válida.")
                        continue
                else:
                    if int(day) > 28:
                        print("Fecha no válida.")
                        continue

            #Comprobar que los días son válidos
            else:
                if int(day) > 30:
                    print("Fecha no válida.")
                    continue

            self.reservationDate=cReservationDate
            break

        #Días de estadía
        while True:
            cDays=input("Introduce la cantidad de días de estadía ")
            #Se elimina cualquier valor no númerico
            cDays.replace("días","") 
            cDays.replace("days","")
            cDays.replace(" ","")
            #Se comprueba que el dia es válido
            if int(cDays)<=0:
                print("Valor no válido")
                continue
            self.stayDays=int(cDays)
             
            break

        #Se calcula el coste total
        cTPrice=int(cDays)*fee
        print("Precio total "+str(cTPrice)+"$")
        self.totalPrice=cTPrice
         
        #Método de pago e Id
        while True:
            cPayMethod=input("Introduce el método de pago a)Efectivo b)Débito c)Crédito ")
            #Se válida que el método de pago sea válido
            if cPayMethod.lower() in ["a","b","c","crédito","credito","débito","debito","efectivo"]:

                if cPayMethod.lower() in ["a","efectivo"]:
                    #Se crea el Id      
                    cId=cName[0].upper()+day+month+year+cDays+"E"
                    self.payMethod="Efectivo"
                    self.id=cId
                elif cPayMethod.lower() in ["b","débito","debito"]:
                    #Se crea el Id
                    cId=cName[0].upper()+day+month+year+cDays+"D"
                    self.payMethod="Débito"
                    self.id=cId
                elif cPayMethod.lower() in ["c","crédito","credito"]:
                    #Se crea el Id
                    cId=cName[0].upper()+day+month+year+cDays+"C"
                    self.payMethod="Crédito"
                    self.id=cId
                break
            else:
                print("Método de pago no válido")
         
        print("Todos los datos del cliente insertados")