def heapify(array, n, i):
    parent = i
    left = 2 * i + 1
    right =  2 * i + 2

    if left < n and array[i] < array[left]:
        parent = left

    if right < n and array[i] < array[right]:
        parent = right

    if parent != i:
        array[i], array[parent] = array[parent], array[i]
        heapify(array, n, parent)

def heap_sort(array):
    n = len(array)

    for i in range(n, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[i], array[0]
        heapify(array, i, 0)
