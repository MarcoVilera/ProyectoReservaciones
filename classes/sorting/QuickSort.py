#TODO Documentar Funcionamiento
def partition(left, right, arr, order,crit1,crit2):
    pivot, ptr = arr[right], left
    for i in range(left, right):
        if order=="asc":
            if crit2=="":
                if getattr(arr[i],crit1) <= getattr(pivot,crit1):
                    arr[i], arr[ptr] = arr[ptr], arr[i]
                    ptr += 1
            else:
              if (getattr(arr[i],crit1) <= getattr(pivot,crit1)) and (getattr(arr[i],crit2)<= getattr(pivot,crit2)):
                    arr[i], arr[ptr] = arr[ptr], arr[i]
                    ptr += 1  
        else:
            if crit2=="":
                if getattr(arr[i],crit1) >= getattr(pivot,crit1):
                    arr[i], arr[ptr] = arr[ptr], arr[i]
                    ptr += 1
            else:
              if (getattr(arr[i],crit1) >= getattr(pivot,crit1)) and (getattr(arr[i],crit2)<= getattr(pivot,crit2)):
                    arr[i], arr[ptr] = arr[ptr], arr[i]
                    ptr += 1
    arr[ptr], arr[right] = arr[right], arr[ptr]
    return ptr

def quicksort(left, right, arr, order,crit1,crit2=""):
    if len(arr) == 1: # Terminating Condition for recursion. VERY IMPORTANT!
        return arr
    if left < right:
        pi = partition(left, right, arr, order,crit1,crit2)
        quicksort(left, pi - 1, arr,order,crit1,crit2) # Recursively sorting the left values
        quicksort(pi + 1, right, arr,order,crit1,crit2) # Recursively sorting the right values
    return arr