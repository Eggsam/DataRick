import random
import time

counter = 0

def mergeSort(lst):
    global counter
    if len(lst) <= 1:
        counter += 1 # increment counter when we dividing array on two
        return lst
    mid = len(lst) // 2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    global counter
    if not left:
        counter += 1 # increment counter when not left (not left - is also comparison)
        return right
    if not right:
        counter += 1 # the same as above for right
        return left
    if left[0] < right[0]:
        counter += 1 # and the final one increment
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])


#lst = [4, 5, 1, 6, 3]
# also you don't need to return counter since you are using global value
#print(merge_sort(lst), counter)

print("For n = 20:")

print("Random Generation of array with 20 elements")

lst = [x for x in range(20)]
random.shuffle(lst)

print("Before Sort:")
print (lst)

print("After Sort:")
start_time = time.time()
mergeSort(lst)
time = time.time() - start_time
print(mergeSort(lst))

print("Comparisions")
print(counter)
print("Time:")
print(str.format('{0:.100f}',time))
