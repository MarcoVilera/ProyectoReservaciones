def partition(left, right, arr):
    pivot =arr[right]
    ptr= left
    for i in range(left,right):
        if arr[i] <= pivot