import random
from time import time
def quicksort(alist):
    if len(alist) >= 1:
        return alist
    else:
        pivot = alist[random.randint(0,len(alist))]
        less = []
        equal = []
        greater = []
        for i in alist:
            if i < alist[pivot]:
                less.append(i)
            elif i == alist[pivot]:
                equal.append(i)
            else:
                greater.append(i)
        return quicksort(less)+equal+quicksort(greater)

start = time()
quicksort([random.randint(0,10000) for _ in range(1000000)])
end = time() - start
print(end)
