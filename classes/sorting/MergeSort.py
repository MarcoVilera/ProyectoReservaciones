import datetime

def dateFilter(arr,min,max):
    #Elimina de una lista de objetos Client los objetos que su atributo reservationDate no esté comprendido en el intervalo min-max
    #arr = Arreglo de objetos clase Client
    #min = Fecha minima del internvalo
    #max = Fecha máxima del intervalo
    output=[]
    #Se recorre el arrglo
    for i in arr:
        #Se crea un objeto datetime para convertir la fecha del objeto Client en una comparable
        reservationDate = datetime.datetime.strptime(i.reservationDate, "%d/%m/%Y")
        #Se hace el mismo tratamiento a min y a max que se hizo con reservationDate
        #Se compara reservationDate con min y max en cada iteración, si no está dentro del intervalo, no se retornará en output
        if reservationDate >= datetime.datetime.strptime(min, "%d/%m/%Y") and reservationDate <= datetime.datetime.strptime(max, "%d/%m/%Y"):
            output.append(i)
    return output

def merge_sort(arr, order):
    #Algoritmo de ordenamiento MergeSort, divide la lista a la mitad, formando dos sublistas y dividiendo estas sublistas 
    #hasta que cada sublista sea de un solo elemento, utilizando la recursión para ordernar la lista
    #arr = arreglo que se usará para el algoritmo
    #order = orden del distribución ("asc" = Ascendente ; "des" = Descendente)
    list_length = len(arr)
    
    if list_length == 1:
        #Condición de parada recursiva
        return arr

    #Se obtiene el punto medio de la lista
    mid_point = list_length // 2

    #se obtiene la mitad izquierda y mitad derecha
    left_partition = merge_sort(arr[:mid_point], order)
    right_partition = merge_sort(arr[mid_point:], order)

    #Recursión indirecta
    return merge(left_partition, right_partition, order)

def merge(left, right, order):
    #Función que se encarga ordenar cada sublista
    #left = sublista de la mitad hacia la izquierda
    #right = sublista de la mitad hacia la derecha
    #order = orden del distribución ("asc" = Ascendente ; "des" = Descendente) 
    output = []
    i = j = 0

    #Mientras que i y j sean menores a la longitud de la sublista
    while i < len(left) and j < len(right):

        if order=="asc":
            #Se compara en orden ascendente las fechas de reservación de cada objeto Client
            if left[i].reservationDate < right[j].reservationDate:
                #Se va formando una nueva lista
                output.append(left[i])
                i += 1
            else:
                output.append(right[j])
                j += 1
            
        else:
            #Se compara en orden descendente
            if left[i].reservationDate>right[j].reservationDate:
                output.append(left[i])
                i+=1
            else:
                output.append(right[j])
                j+=1
    #Se van agregando los elementos ordenados a la lista
    output.extend(left[i:])
    output.extend(right[j:])
    return output
