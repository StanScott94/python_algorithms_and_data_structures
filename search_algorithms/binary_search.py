def binary_search(item_to_find, array, start=0, end=None):

    if end is None:
        end = len(array) - 1

    if start > end:
        return None
    else:
        centre = (start + end) // 2
        if item_to_find == array[centre]:
            return array[centre], centre
        elif item_to_find > array[centre]:
            return binary_search(item_to_find, array, centre+1, end)
        else:
            return binary_search(item_to_find, array, start, centre-1)
