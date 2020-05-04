def insertion_sort(array):
    for index in range(1, len(array)):
        if array[index] < array[index -1]:
             for reverse_index in range(index, 0, -1):
                if array[reverse_index] < array[reverse_index -1]:
                    array[reverse_index], array[reverse_index -1] = array[reverse_index -1], array[reverse_index]
