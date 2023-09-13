def heapify(arr, n, i, order):
    #Crea un heap(monticulo) a partir del elemento en la posición i
    #arr = arreglo que se usará en el algoritmo heapSort
    #n = tamaño de la lista
    #order = orden del distribución ("asc" = Ascendente ; "des" = Descendente)

    father = i  
    #Hijo izquierdo del nodo actual
    l = 2 * i + 1
    #Hijo derecho del nodo actual  
    r = 2 * i + 2

    #En función del orden evaluará si el hijo izquierdo es mayor o menor al nodo actual, si lo es, cambiará el indice del elemento mas grande o pequeño de acuerdo al orden
    if l < n and (order=="asc" and arr[i].stayDays < arr[l].stayDays or not order=="asc" and arr[i].stayDays > arr[l].stayDays):
        father = l
    #En función del orden evaluará si el hijo derecho es mayor o menor al nodo actual, si lo es, cambiará el indice del elemento mas grande o pequeño de acuerdo al orden
    if r < n and (order=="asc" and arr[father].stayDays < arr[r].stayDays or not order=="asc" and arr[father].stayDays > arr[r].stayDays):
        father = r

    #Si el elemento más grande ya no es el inicial, se intercambian los valores 
    if father != i:
        arr[i], arr[father] = arr[father], arr[i]  # swap

        # Llamada recursiva para reordenar el arbol
        heapify(arr, n, father, order)

def heapSort(arr,order):
    #Utiliza el algoritmo heapSort a partir de una lista de objetos Cliente,  en orden ascendente o descendiente
    #arr = arreglo que se usará en el algoritmo heapSort
    #order = orden del distribución ("asc" = Ascendente ; "des" = Descendente)
    n = len(arr)

    #Crea un heap(monticulo) a partir de toda la lista
    for i in range((n // 2) - 1, -1, -1):
        heapify(arr, n, i,order)

    #Recorre la lista desde el final hasta el principio, intercambiando el elemento actual con el elemento más grande del heap y luego reordenando el heap.
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0,order)

