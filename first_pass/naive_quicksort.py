import random
from time import time
def quick_sort(alist):
    if len(alist) <= 1:
        return alist
    else:
        less = []
        equal = []
        greater = []
        pivot = alist[0]
        for i in alist:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                greater.append(i)
        return quick_sort(less)+equal+quick_sort(greater)

#start = time()
quick_sort([random.randint(0,10000) for _ in range(1000000)])
#end = time() - start
#print(end)
