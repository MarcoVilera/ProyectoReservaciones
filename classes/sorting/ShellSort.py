def shellSort(array, n, order):
# Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and (not order=="asc" and array[j - interval] < temp or order=="asc" and array[j - interval] > temp):
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2