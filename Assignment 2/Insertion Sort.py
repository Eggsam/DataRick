import time
import random

start = time.time()

def insertionSort(arr):
    k = 0
    n = len(arr) - 1
    comparisons = 0
    while k+1 <= n:
        i = k+1
        curr_val = arr[i]
        comparisons += 1
        while i>0 and arr[i-1] > curr_val:
            arr[i] = arr[i-1]
            i=i-1
            comparisons += 1
        arr[i] = curr_val
        k = k + 1
    return comparisons

print("For n = 1000: \nRandom Generation of Array: ")
y = 200
arr =[random.randint(1,1000) for x in range(y)]
random.shuffle(arr)
print("Before Sort: \n", arr)

print("After Sort:")
insertionSort(arr)
end = time.time()
print(arr," \nComparisions", insertionSort(arr), "\nTime: " , (end-start))
