import random
from time import time
def quicksort(alist,start,end):
    if start < end:
        pivot = partition(alist,start,end)
        quicksort(alist,start,pivot-1)
        quicksort(alist,pivot+1,end)
        
def partition(alist,first,last):
    pivot = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivot:
            leftmark += 1
        while alist[rightmark] >= pivot and rightmark >= leftmark:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark]
    alist[first],alist[rightmark] = alist[rightmark],alist[first]
    return rightmark
            
start = time()
quicksort([random.randint(0,10000) for _ in range(1000000)],0,1000000-2)
end = time() - start
print(end)
