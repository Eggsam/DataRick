import random
import time
import sys


start = time.time()

def selectionSort(arr):
    count = 0
    for index in range(len(arr)):
        min = index
        count += 1
        # Find the index'th smallest element
        for scan in range(index + 1, len(arr)):
            if (arr[scan] < arr[min]):
                min = scan
        if min != index: # swap the elements
            arr[index], arr[min] = arr[min], arr[index]
    return count, arr


#A = [1,2,3,4,5,6,64, 25, 12, 22, 10, 15, 70, 1001]
#print("comparisons = ", selection(A))

print("For n = 1000: \nRandom Generation of Array: ")
y = 100
arr =[random.randint(1,1000) for x in range(y)]
random.shuffle(arr)
print("Before Sort: \n", arr)

print("After Sort:")
selectionSort(arr)
end = time.time()
print(arr," \nComparisions", selectionSort(arr), "\nTime: " , (end-start))
