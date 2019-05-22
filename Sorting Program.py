import random
import time


def bubbleSort(arr):

    n = len(arr)
    comparisons = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return (comparisons)

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
    return count

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

def mergeSort(arr):
    comparisons = 0
    if len(arr)>1:
        mid = len(arr)//2
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]

        leftPart = mergeSort(leftHalf)
        rightPart = mergeSort(rightHalf)
        comparisons += leftPart + rightPart #ask about this

        i=j=k=0
        while i < len(leftHalf) and j < len(rightHalf):
            comparisons += 1
            if leftHalf[i] < rightHalf[j]:
                arr[k]=leftHalf[i]
                i=i+1
            else:
                arr[k]=rightHalf[j]
                j=j+1
            k=k+1

        while i < len(leftHalf):
            arr[k]=leftHalf[i]
            i=i+1
            k=k+1


        while j < len(rightHalf):
            arr[k]=rightHalf[j]
            j=j+1
            k=k+1


    return comparisons

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

userInput = input("What would you like the size of the array to be? ")
y = int(userInput)

print("For n = 1000: \nRandom Generation of Array: ")
arr =[random.randint(1,1000) for x in range(y)]
random.shuffle(arr)

print("Before Sort: \n", arr)
sortChoice = input("What sorting algorithm would you like to use? ")
#while True:
#    try:
#        if sortChoice == "bubbleSort"or "quickSort"or"selectionSort"or"insertionSort"or"heapSort"or"mergeSort":
#            continue
#    except ValueError:
#        print("error")
if sortChoice == "bubbleSort":
    start = time.time()
    sortChoice = (bubbleSort(arr))
    end = time.time()
elif sortChoice == "quickSort":
    start = time.time()
    sortChoice = (quicksort(arr))
    end = time.time()
elif sortChoice == "selectionSort":
    start = time.time()
    sortChoice = (selectionSort(arr))
    end = time.time()
elif sortChoice == "insertionSort":
    start = time.time()
    sortChoice = (insertionSort(arr))
    end = time.time()
elif sortChoice == "mergeSort":
    start = time.time()
    sortChoice = (mergeSort(arr))
    end = time.time()
elif sortChoice == "heapSort":
    start = time.time()
    sortChoice = (heapSort(arr))
    end = time.time()
#sortChoice(arr)
print("After Sort:" , arr)
print(" \nComparisions", sortChoice,  "\nTime: ", end-start )
