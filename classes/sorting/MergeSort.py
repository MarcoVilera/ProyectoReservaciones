#TODO Documentar Código
def merge_sort(list, order):

    list_length = len(list)

    if list_length == 1:
        return list

    mid_point = list_length // 2

    left_partition = merge_sort(list[:mid_point], order)
    right_partition = merge_sort(list[mid_point:], order)

    return merge(left_partition, right_partition, order)

def merge(left, right, order):

    output = []
    i = j = 0

    while i < len(left) and j < len(right):

        if order=="asc":
            if left[i] < right[j]:

                output.append(left[i])

                i += 1
            else:
                output.append(right[j])
                j += 1
        else:
            if left[i]>right[j]:
                output.append(left[i])
                i+=1
            else:
                output.append(right[j])
                j+=1

    output.extend(left[i:])
    output.extend(right[j:])
    return output