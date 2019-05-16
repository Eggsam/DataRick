import time

start = time.time()

def heapify(arr, n, i):
    count = 0
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
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

arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is")
for i in range(n): 
    print ("%d" %arr[i])

compar = (heapSort(arr))+ (heapify(arr,n,i))
print ("The number of comparisons is" , compar)
end = time.time()
x =end - start 
print("\nThe run time is", str(x), "Ms")

