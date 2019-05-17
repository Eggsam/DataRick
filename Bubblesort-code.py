def bubblesort(arr):
    n = len(arr)
    comparisons = 0
    for i in range(n):

        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    for i in range(len(arr)):
        print("%d" %arr[i])
    
    return (comparisons)

arr=[1,9,3,2,7,4,6,11,10,19,33,22,27,21,14,17,5,99,54,43]

print("The number of comparisons is" , bubblesort(arr))

