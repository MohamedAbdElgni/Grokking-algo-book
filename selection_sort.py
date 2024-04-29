def find_(arr, smallest=True):
    """
    Helper function to return the min or the max
    :param arr:
    :param smallest: bool :default True
    :return: the index fo the element smallest or largest
    """
    if smallest:
        value = min(arr)
    else:
        value = max(arr)
    _index = arr.index(value)
    return _index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        value = find_(arr, smallest=False)
        new_arr.append(arr.pop(value))
    return new_arr


print(selection_sort([5, 3, 6, 2, 10]))
