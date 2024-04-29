def sum_(arr):
    total = 0
    for x in arr:
        total += x
    print(total)


def get_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + get_sum(arr[1:])


print(get_sum([10, 2, 30, 40, 50]))
