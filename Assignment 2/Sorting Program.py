import random
import time


def bubbleSort(arr): #standard bubble sort

    n = len(arr) #get length of array
    comparisons = 0 #initialize comparisons
    for i in range(n):
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                comparisons += 1 #comparisons counter
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return (comparisons) #number of comparisons

def shortBubbleSort(arr): #improved bubble sort
    exchanges = True
    passnum = len(arr)-1 #get length of array - 1
    comparisons = 0 #initialize comparisons
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):

           if arr[i]>arr[i+1]:
               comparisons+=1 #comparisons counter
               exchanges = True
               temp = arr[i]
               arr[i] = arr[i+1]
               arr[i+1] = temp
       passnum = passnum-1
       return comparisons #number of comparisons

def _partition(arr, start, end): #partition for quick sort
    count = 0 #initialize comparisons
    pos = start
    for i in range(start, end):
        count += 1 #comparisons counter
        if arr[i] < arr[end]:
            arr[i], arr[pos] = arr[pos], arr[i]
            pos += 1
    arr[pos], arr[end] = arr[end], arr[pos]
    return pos, count #number of comparisons and position

def _quicksort(arr, start, end): #quick sort helper
    count = 0 #initialize comparisons
    if start < end:
        pos, count = _partition(arr, start, end)
        count += _quicksort(arr, start, pos - 1) #comparisons counter
        count += _quicksort(arr, pos + 1, end) #comparisons counter
    return count #number of comparisons

def quickSort(arr, start=None, end=None): #quick sort algorithm
    if start is None:
        start = 0
    if end is None:
        end = len(arr) - 1 #get length of array - 1
    return _quicksort(arr, start, end)

def selectionSort(arr): #selection sort algorithm
    count = 0 #initialize comparisons
    for index in range(len(arr)- 1): #get length of array-1
        min = index
        count +=1 #comparisons counter
        for scan in range(index + 1, len(arr)): #Find the index'th smallest element and #get length of array -1
            count += 1
            if (arr[scan] < arr[min]):
                min = scan
        if min != index: # swap the elements
            arr[index], arr[min] = arr[min], arr[index]
    return count #number of comparisons

def insertionSort(arr): #insertion sort algorithm
    k = 0
    n = len(arr) - 1 #get length of array -1
    comparisons = 0
    while k+1 <= n:
        i = k+1
        curr_val = arr[i]
        comparisons += 1 #comparisons counter
        while i>0 and arr[i-1] > curr_val:
            arr[i] = arr[i-1]
            i=i-1
            comparisons += 1 #comparisons counter
        arr[i] = curr_val
        k = k + 1
    return comparisons #number of comparisons

def mergeSort(arr): #merge sort algorithm
    comparisons = 0 #initialize comparisons
    if len(arr)>1: #get length of array where its greater than 1
        mid = len(arr)//2 ##get length of array divided by 2
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]

        leftPart = mergeSort(leftHalf) #call algorithm to sort left half
        rightPart = mergeSort(rightHalf) #call algorithm to sort right half
        comparisons += leftPart + rightPart #comparisons counter
        i=j=k=0 #initialize variables
        while i < len(leftHalf) and j < len(rightHalf):
            comparisons += 1 #comparisons counter
            if leftHalf[i] < rightHalf[j]: #if left greater than right
                arr[k]=leftHalf[i]
                i=i+1
            else:
                arr[k]=rightHalf[j]
                j=j+1
            k=k+1

        while i < len(leftHalf): #while i is less than the length of left half
            arr[k]=leftHalf[i]
            i=i+1
            k=k+1

        while j < len(rightHalf): #while j is less than the length of right half
            arr[k]=rightHalf[j]
            j=j+1
            k=k+1

    return comparisons #number of comparisons

def heapify(arr, n, i): #heap sort helper
    count = 0 #initialize comparisons
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]: #if l is greater than n and arr i greather than arr l
        largest = l
    if r < n and arr[largest] < arr[r]: #if r is greater than n and arr i is great thatn arr r
        largest = r
    if  largest != i:
        count += 1 #comparisons counter
        arr[i],arr[largest] = arr[largest],arr[i]
        count += heapify(arr, n, largest) #comparisons counter
    return count #number of comparisons

def heapSort(arr): #heap sort algorithm

    n = len(arr) #get length of array
    count = 0 #initialize comparisons
    for i in range(n, -1, -1):
        heapify(arr, n, i) #calls healper function for algorithm
        count += heapify(arr, i, 0) #comparisons counter
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        count += heapify(arr, i, 0) #comparisons counter

    return count #number of comparisons

userInput = input("What would you like the size of the array to be? ")
y = int(userInput) #stores user inputer

print("For n = 1000: \nRandom Generation of Array: ")
arr =[random.randint(1,1000) for x in range(y)] #generates random array
random.shuffle(arr) # shuffles array

print("Before Sort: \n", arr) #print array before sort
sortChoice = input("What sorting algorithm would you like to use? ") #choose algorithm to sort with

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
elif sortChoice == "shortBubbleSort":
    start = time.time()
    sortChoice = (shortBubbleSort(arr))
    end = time.time()

print("After Sort:" , arr) #print sorted array
print(" \nComparisions", sortChoice,  "\nTime: ", end-start ) #print number of comparisons and time
