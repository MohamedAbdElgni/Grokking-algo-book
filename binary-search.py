def bin_search(items, i):
    counter = 0
    start = 0
    end = len(items)-1
    while end > start:
        mid = round((start+end) / 2)
        search = items[mid]
        if search == i:
            print(f"Counter {counter}")
            return search
        elif search > i:
            end = mid
        elif search < i:
            start = mid
        counter += 1
    print(f"Counter {counter}")
    return None
mylist = range(0,12045450000000)
print(bin_search(mylist, 7))
