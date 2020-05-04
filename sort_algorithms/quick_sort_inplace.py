from random import randint

def partition(array, start, end):

    i = start -1
    pivot = array[end]

    for j in range(start, end):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i +1], array[end] = array[end], array[i +1]
    return i +1

def quick_sort_inplace(array, start=0, end=None):

    if end is None:
        end = len(array) - 1
    if start < end:
        pivot = partition(array, start, end)
        quick_sort_inplace(array, start, pivot - 1)
        quick_sort_inplace(array, pivot + 1, end)
        return array
