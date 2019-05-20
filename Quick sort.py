import random
import time

start = time.time()

def _partition(arr, start, end):
    count = 0
    pos = start
    for i in range(start, end):
        count += 1
        if arr[i] < arr[end]:
            arr[i], arr[pos] = arr[pos], arr[i]
            pos += 1
    arr[pos], arr[end] = arr[end], arr[pos]
    return pos, count

def _quicksort(arr, start, end):
    count = 0
    if start < end:
        pos, count = _partition(arr, start, end)
        count += _quicksort(arr, start, pos - 1)
        count += _quicksort(arr, pos + 1, end)
    return count

def quickSort(arr, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(arr) - 1
    return _quicksort(arr, start, end)


print("For n = 1000: \nRandom Generation of Array: ")
y = 100
arr =[random.randint(1,1000) for x in range(y)]
random.shuffle(arr)
print("Before Sort: \n", arr)

print("After Sort:")
quickSort(arr)
end = time.time()
print(arr," \nComparisions", quickSort(arr), "\nTime: " , (end-start))
