import random
import time


def _partition(mylist, start, end):
    count = 0
    pos = start
    for i in range(start, end):
        count += 1
        if mylist[i] < mylist[end]:
            mylist[i], mylist[pos] = mylist[pos], mylist[i]
            pos += 1
    mylist[pos], mylist[end] = mylist[end], mylist[pos]
    return pos, count

def _quicksort(mylist, start, end):
    count = 0
    if start < end:
        pos, count = _partition(mylist, start, end)        
        count += _quicksort(mylist, start, pos - 1)
        count += _quicksort(mylist, pos + 1, end)
    return count

def quickSort(mylist, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(mylist) - 1
    return _quicksort(mylist, start, end)

print("For n = 20:")

print("Random Generation of array with 20 elements")

mylist = [x for x in range(20)]
random.shuffle(mylist)


print("Before Sort:")
print (mylist)

print("After Sort:")
start_time = time.time()
quickSort(mylist)
time = time.time() - start_time
print(mylist)

print("Comparisions")
print(quickSort(mylist))
print("Time:")
print(str.format('{0:.6f}',time))
