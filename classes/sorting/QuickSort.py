#TODO Documentar Funcionamiento
def partition(left, right, arr, order):
    pivot, ptr = arr[right], left
    for i in range(left, right):
        if order=="asc":
            if arr[i] <= pivot:
                arr[i], arr[ptr] = arr[ptr], arr[i]
                ptr += 1
        else:
            if arr[i] >= pivot:
                arr[i], arr[ptr] = arr[ptr], arr[i]
                ptr += 1
    arr[ptr], arr[right] = arr[right], arr[ptr]
    return ptr

def quicksort(left, right, arr, order):
    if len(arr) == 1: # Terminating Condition for recursion. VERY IMPORTANT!
        return arr
    if left < right:
        pi = partition(left, right, arr, order)
        quicksort(left, pi - 1, arr,order) # Recursively sorting the left values
        quicksort(pi + 1, right, arr,order) # Recursively sorting the right values
    return arr