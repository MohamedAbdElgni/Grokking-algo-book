import time


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


def quick_sort(arr, left, right):
    if left < right:
        partition_idx = partition(arr, left, right)
        quick_sort(arr, left, partition_idx - 1)
        quick_sort(arr, partition_idx + 1, right)


arr = [66, 18, 500, 23, 214, 154, 887, 5]
start_time = time.time()
quick_sort(arr, 0, len(arr) - 1)
print(f"End Time: {time.time() - start_time}")
print(arr)

