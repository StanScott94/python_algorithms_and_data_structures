def bubble_sort(array):
    arraySorted = False
    while not arraySorted:
        arraySorted = True
        for index in range(len(array) -1):
            if array[index] > array[index +1]:
                array[index], array[index +1] = array[index +1], array[index]
                arraySorted = False
    return array
