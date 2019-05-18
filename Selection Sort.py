import sys 
 
  
def selection(A):
    comparison = 0
    for i in range(len(A)): 
      
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j
                comparison += 1
                     
        A[i], A[min_idx] = A[min_idx], A[i] 

    
    print ("Sorted array") 
    for i in range(len(A)): 
        print("%d" %A[i]),

    return (comparison)

A = [1,2,3,4,5,6,64, 25, 12, 22, 10, 15, 70, 1001]
print("comparisons = ", selection(A))
