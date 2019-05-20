import random
import time

start = time.time()

def bubbleSort(arr):
    n = len(arr)
    comparisons = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return (comparisons)

print("For n = 1000: \nRandom Generation of Array: ")
y = 100
arr =[random.randint(1,100) for x in range(y)]
random.shuffle(arr)
print("Before Sort: \n", arr)

print("After Sort:")
bubbleSort(arr)
end = time.time()
print(arr," \nComparisions", bubbleSort(arr), "\nTime: " , (end-start))
