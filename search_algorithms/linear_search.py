def linear_search(item_to_find, array):
    for index in range(len(array)):
        if item_to_find == array[index]:
            return array[index], index
