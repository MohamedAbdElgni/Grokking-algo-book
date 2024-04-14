def find_(arr, smallest=True):
    """
    Helper function to return the min or the max
    :param arr:
    :param smallest: bool :default True
    :return: the index fo the element smallest or largest
    """
    if smallest:
        smallest_value = min(arr)
    else:
        smallest_value = max(arr)
    smallest_index = arr.index(smallest_value)
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_(arr, smallest=False)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort([5, 3, 6, 2, 10]))
