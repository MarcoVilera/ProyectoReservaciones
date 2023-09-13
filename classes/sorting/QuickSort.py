def quicksort(left, right, arr, order,crit1,crit2=""):
    #Algoritmo de QuickSort, utiliza un pivote para ordernar tanto el extremo izquierdo de una lista como el derecho, 
    # y cambiando el pivote hasta que la lista esté ordenada
    #left = Elemento en el extremo izquierdo
    #right = Elemento en el extremo derecho
    #arr = arreglo que se usará en el algoritmo
    #order = orden de distribución ("asc"= Ascendente ; "des" = Descendente)
    #crit1 = criterio de ordenamiento (en función de que atributo se ordenará la lista)
    #crit2 = criterio opcional para ordenamiento con criterios  multiples

    if len(arr) == 1: 
        #Condición de parada recursiva
        return arr
    if left < right:
        #Obtiene la partición
        pi = partition(left, right, arr, order,crit1,crit2)

        #Ordena recursivamente el lado derecho
        quicksort(left, pi - 1, arr,order,crit1,crit2)

        #Ordena recursivamente el lado izquierdo
        quicksort(pi + 1, right, arr,order,crit1,crit2) 
    return arr

def partition(left, right, arr, order,crit1,crit2):
    #Particiona una lista en función de sus extremos tanto izquierdo como derecho
    #left = Elemento en el extremo izquierdo
    #right = Elemento en el extremo derecho
    #arr = arreglo que se usará en el algoritmo
    #order = orden de distribución ("asc"= Ascendente ; "des" = Descendente)
    #crit1 = criterio de ordenamiento (en función de que atributo se ordenará la lista)
    #crit2 = criterio opcional para ordenamiento con criterios  multiples

    #El elemento del extremo derecho se transforma en el pivote
    #El elemento del extremo izquierdo se utilizará para mantener un registro de elementos menores o iguales al pivote
    pivot, ptr = arr[right], left
    
    for i in range(left, right):
        #En caso de ser orden ascendente"
        if order=="asc":
            #Busqueda por un solo criterio
            if crit2=="":
                #Si i es menor o igual al pivote, este se convertura en el pivote y el antiguo pivote se insertará en el indice antiguo del nuevo pivote
                if getattr(arr[i],crit1) <= getattr(pivot,crit1):
                    arr[i], arr[ptr] = arr[ptr], arr[i]
                    ptr += 1

            #Busqueda por multiples criterios, se comparan ambos para cambiar el pivote
            else:
              if (getattr(arr[i],crit1) <= getattr(pivot,crit1)) and (getattr(arr[i],crit2)<= getattr(pivot,crit2)):
                    arr[i], arr[ptr] = arr[ptr], arr[i]
                    ptr += 1  
        #Orden descendente
        else:
            #Busqueda por un solo criterio
            if crit2=="":
                #Si i es mayor o igual al pivote, este se convertura en el pivote y el antiguo pivote se insertará en el indice antiguo del nuevo pivote
                if getattr(arr[i],crit1) >= getattr(pivot,crit1):
                    arr[i], arr[ptr] = arr[ptr], arr[i]
                    ptr += 1
                #Busqueda por multiples criterios, se comparan ambos para cambiar el pivote
            else:
              if (getattr(arr[i],crit1) >= getattr(pivot,crit1)) and (getattr(arr[i],crit2)<= getattr(pivot,crit2)):
                    arr[i], arr[ptr] = arr[ptr], arr[i]
                    ptr += 1
    #Se intercambian las posiciones
    arr[ptr], arr[right] = arr[right], arr[ptr]
    return ptr