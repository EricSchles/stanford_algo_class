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

        
print(quick_sort([4,3,2,1,5,6,1,2,3]))
