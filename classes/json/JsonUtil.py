import json
def ReadData(path):
    with open(path,"r") as content:
       data = json.load(content)
       content.close()
   
    return data

def WriteData(path, data):
    with open(path, "r") as content:
        # Lee el contenido del archivo JSON
        try:
            data_json = json.load(content)
        except json.JSONDecodeError:
            data_json = []
        content.close()

    # Agrega la data al final del archivo JSON
    data_json.append(data)

    # Escribe el archivo JSON con los datos agregados
    with open(path, "w") as content:
        json.dump(data_json, content)
        content.close()
