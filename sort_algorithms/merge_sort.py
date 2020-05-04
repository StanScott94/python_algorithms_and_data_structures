def merge_sorted_lists(array1, array2):
    sorted_array = []
    index1, index2 = 0, 0

    while index1 < len(array1) and index2 < len(array2):
         if array1[index1] < array2[index2]:
            sorted_array.append(array1[index1])
            index1 += 1
         else:
            sorted_array.append(array2[index2])
            index2 += 1

    if  index1 < len(array1):
        sorted_array.extend(array1[index1 : len(array1)])
    else:
        sorted_array.extend(array2[index2 : len(array2)])

    return sorted_array

def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left_array = merge_sort(array[:middle])
        right_array = merge_sort(array[middle:])
        return merge_sorted_lists(left_array, right_array)
