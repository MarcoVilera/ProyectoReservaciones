def shellSort(array, n, order,atr):
#Algoritmo de Shellsort, Ordena la lista en diversos intervalos cada vez mas pequeños
#array = arreglo que se utilizará en el algoritmo Shellsort
#n = tamaño del arreglo
#order = orden de distribución ("asc"= Ascendente ; "des" = Descendente)
    #Se crea el primer intervalo
    interval = n // 2
    while interval > 0:
        #Mientras el intervalo sea mayor a 0
        for i in range(interval, n):
            #Recorre la lista desde el intervalo actual hasta n
            temp = array[i]
            #El temporal toma el valor del elemento que es igual al indice del inicio del intervalo
            j = i

            while j >= interval and (not order=="asc" and getattr(array[j - interval],atr)< getattr(temp,atr) or order=="asc" and getattr(array[j - interval],atr) > getattr(temp,atr)):
                #Mientras que j sea mayor o igual al intervalo, se evalua si el orden es ascendente o descendente 
                #y si el elemento en el indice j dependiendo del orden sea mayor o menor que el elemento actual, se intercambiaran
                array[j] = array[j - interval]
                #Se reduce j en función del intervalo
                j -= interval
            #El elemento en la posición j se convierte en el nuevo temporal
            array[j] = temp
        #Se reduce el intervalo
        interval //= 2