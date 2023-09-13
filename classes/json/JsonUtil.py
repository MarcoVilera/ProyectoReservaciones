import json

def ReadData(path):
    #Lee un archivo .json, y si no existe lo crea
    #path = Ruta donde se aloja el archivo .json

    try:
    #Intenta abrir el archivo
        with open(path, "r",encoding="utf-8") as content:
            data = json.load(content)

    #Si no lo encuentra, crea el archivo con unas [] dentro
    except FileNotFoundError:
        with open(path, "w") as content:
            data = []
            content.write(json.dumps(data))
    
    #Si el archivo está vacio, introduce en el archivo unas []
    except json.JSONDecodeError:
        with open(path, "w") as content:
            data = []
            content.write(json.dumps(data))

    #Retorna el contenido del archivo .json
    return data

def WriteData(path, data):
    #Abre y lee un archivo .json
    #path = Ruta del archivo .json
    #data = Datos que se quieren ingresar en el arcihvo .json DEBE SER UN DICCIONARIO

    with open(path, "r",encoding="utf-8") as content:
        #Intenta abrir el archivo
        try:
            dataJson = json.load(content)
        #Si está vacio crea una lista vacia
        except json.JSONDecodeError:
            dataJson = []
        content.close()

        #Carga los datos ingresados por parametro
    dataJson.append(data)

    # Escribe el archivo JSON con los datos agregados
    with open(path, "w",encoding="utf-8") as content:
        json.dump(dataJson, content,default=lambda cls:cls.__dict__, indent=3)
        content.close()
