def selection_sort(array):
    spotIndex = 0
    while spotIndex < len(array):
        for arrayIndex in range(spotIndex, len(array)):
            if array[spotIndex] > array[arrayIndex]:
                 array[arrayIndex], array[spotIndex] = array[spotIndex], array[arrayIndex]
        spotIndex += 1
