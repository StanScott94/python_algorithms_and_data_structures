def quick_sort_basic(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[-1]
        smaller, equal, larger = [], [], []
        for number in array:
            if number < pivot:      smaller.append(number)
            elif number == pivot:   equal.append(number)
            else:                   larger.append(number)
            
        return quick_sort_basic(smaller) + equal + quick_sort_basic(larger)
