import time


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    # pivot = arr[len(arr) // 2]
    pivot = arr[0]
    left = [el for el in arr[1:] if el <= pivot]
    right = [el for el in arr[1:] if el > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


start_time = time.time()

print(quick_sort([66, 18, 500, 23, 214, 154, 887, 5]))

print(f"End Time: {time.time() - start_time}")
