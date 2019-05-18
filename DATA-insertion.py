import time




def insertionSort(arr): 
    start = time.time()
    comparisons = 0
    for i in range(1, len(arr)): 
  
        key = arr[i]
        
         
        
        j = i-1


        
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
                comparisons += 1
        arr[j + 1] = key

    for i in range(len(arr)): 
        print ("% d" % arr[i])

    
    end = time.time()
    print("The run time is" , end-start )
    return(comparisons)
    #return (end-start)


arr = [5, 6, 13, 12, 11] 
print("The number of comparisions is",insertionSort(arr)) 

