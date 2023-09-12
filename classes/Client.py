import re

#TODO Documentar codigo
class Client:
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
        
        print("Introducir datos del cliente")
        while True:
            cName=input("Introduce el nombre del cliente ")
            cLastN=input("Introduce el apellido del cliente ")
            if re.search(r"[^a-zA-ZñÑáéíóúÁÉÍÓÚ\s]", cName):
                print("El nombre no puede contener números o caracteres especiales")
                continue 
            elif re.search(r"[^a-zA-ZñÑáéíóúÁÉÍÓÚ\s]", cLastN):
                print("El apellido no puede contener números o caracteres especiales") 
                continue
            else:
                self.fName=cName.capitalize()
                self.lName=cLastN.capitalize()
                 
                break
                
        while True:
            cIdentification = input("Introduce la cédula del cliente ")
            cIdentification = cIdentification.replace(".", "")
            if re.search(r"^([0-9]{6,8})$", cIdentification):
                self.identification=cIdentification
                 
                break
            elif len(cIdentification)<=5 or len(cIdentification)>=9:
                print("La cédula debe tener al menos 6 digitos y máximo 8")
            else:
                print("La cédula no puede contener caracteres especiales o alfanumericos")

        while True:
            cEmail=input("Introduce el correo electronico del cliente ")
            if re.search(r"^[a-zA-Z0-9][a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$", cEmail):
                self.email=cEmail
                 
                break
            else:
                print("Correo electronico no valido")

        while True:
            cReservationDate = input("Introduce la fecha de reservación del cliente en el siguiente formato dd/mm/aaaa: ")

            if not re.search(r"^([0-3]{1}[0-9]{1})/([0-1]{1}[0-9]{1})/([0-9]{4})$", cReservationDate):
                print("Fecha no válida.")
                continue

            day, month, year = cReservationDate.split("/")
            if month in ["01", "03", "05", "07", "08", "10", "12"]:
                if int(day) > 31:
                    print("Fecha no válida.")
                    continue
            elif int(month)>12 or int(month)<1:
                print("Fecha no válida.")

            elif month == "02":
                if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
                    if int(day) > 29:
                        print("Fecha no válida.")
                        continue
                else:
                    if int(day) > 28:
                        print("Fecha no válida.")
                        continue
            else:
                if int(day) > 30:
                    print("Fecha no válida.")
                    continue
        
            if month[0]=="0":
                month.replace("0","")
            self.reservationDate=cReservationDate
             
            break

        while True:
            cDays=input("Introduce la cantidad de dias de estadia ")
            cDays.replace("dias","") 
            cDays.replace("days","")
            cDays.replace(" ","")
            if int(cDays)<=0:
                print("Valor no valido")
                continue
            self.stayDays=int(cDays)
             
            break

        cTPrice=int(cDays)*fee
        print("Precio total "+str(cTPrice)+"$")
        self.totalPrice=cTPrice
         
        while True:
            cPayMethod=input("Introduce el método de pago a)Efectivo b)Débito, c)Crédito ")
            if cPayMethod.lower() in ["a","b","c","crédito","credito","débito","debito","efectivo"]:

                if cPayMethod.lower() in ["a","efectivo"]:      
                    cId=cName[0].upper()+day+month+year+cDays+"E"
                    self.payMethod=="Efectivo"
                    self.id=cId
                elif cPayMethod.lower() in ["b","débito","debito"]:
                    cId=cName[0].upper()+day+month+year+cDays+"D"
                    self.payMethod=="Débito"
                    self.id=cId
                elif cPayMethod.lower() in ["c","crédito","credito"]:
                    cId=cName[0].upper()+day+month+year+cDays+"C"
                    self.payMethod="Crédito"
                    self.id=cId
                break
            else:
                print("método no valido")
         
        print("Todos los datos del cliente insertados")