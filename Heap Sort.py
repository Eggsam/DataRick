import random
import time

start = time.time()
#HeapSort Algorithm
def heapify(arr, n, i):
    count = 0
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if  largest != i:
        count += 1
        arr[i],arr[largest] = arr[largest],arr[i]
        count += heapify(arr, n, largest)
    return count

def heapSort(arr):

    n = len(arr)
    count = 0
    for i in range(n, -1, -1):
        heapify(arr, n, i)
        count += heapify(arr, i, 0)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        count += heapify(arr, i, 0)

    return count

print("For n = 1000: \nRandom Generation of Array: ")
#arr = [x for x in range(20)]
y = 100
arr =[random.randint(1,100) for x in range(y)]
random.shuffle(arr)
print("Before Sort: \n", arr)

print("After Sort:")
heapSort(arr)
end = time.time()
print(arr," \nComparisions", heapSort(arr), "\nTime: " , (end-start))
