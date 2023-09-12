import json
#TODO Documentar funcionamiento métodos
def ReadData(path):
    try:
        with open(path, "r",encoding="utf-8") as content:
            data = json.load(content)
            
    except FileNotFoundError:
        with open(path, "w") as content:
            data = []
            content.write(json.dumps(data))
            
    except json.JSONDecodeError:
        with open(path, "w") as content:
            data = []
            content.write(json.dumps(data))
    return data

def WriteData(path, data):
    with open(path, "r",encoding="utf-8") as content:
        # Lee el contenido del archivo JSON
        try:
            data_json = json.load(content)
        except json.JSONDecodeError:
            data_json = []
        content.close()

    # Agrega la data al final del archivo JSON
    data_json.append(data)

    # Escribe el archivo JSON con los datos agregados
    with open(path, "w",encoding="utf-8") as content:
        json.dump(data_json, content,default=lambda cls:cls.__dict__, indent=3)
        content.close()
