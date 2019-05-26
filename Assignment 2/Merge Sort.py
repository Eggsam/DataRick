import random
import time
start = time.time()

def mergeSort(arr):
    comparisons = 0
    if len(arr)>1:
        mid = len(arr)//2
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]

        leftPart = mergeSort(leftHalf)
        rightPart = mergeSort(rightHalf)
        comparisons += leftPart + rightPart


        #comparisons += leftPart + rightPart #ask about this
        i=j=k=0

        while i < len(leftHalf) and j < len(rightHalf):

            if leftHalf[i] < rightHalf[j]:
                arr[k]=leftHalf[i]
                i=i+1
                comparisons +=1
            else:
                arr[k]=rightHalf[j]
                j=j+1
                comparisons +=1

            k=k+1


        while i < len(leftHalf):
            arr[k]=leftHalf[i]
            i=i+1
            k=k+1
            #comparisons += 1

        while j < len(rightHalf):
            arr[k]=rightHalf[j]
            j=j+1
            k=k+1
            #comparisons += 1

    return comparisons

print("For n = 1000: \nRandom Generation of Array: ")
y = 4
arr =[random.randint(1,10) for x in range(y)]

random.shuffle(arr)
print("Before Sort: \n", arr)

print("After Sort:")
mergeSort(arr)
end = time.time()
print(arr," \nComparisions", mergeSort(arr), "\nTime: " , (end-start))
