def class_qsort(alist):
    left = 0
    right = len(alist)-1
    while left < right:
        mid = (right - left)//2
        partition(alist,left,mid)
        partition(alist,mid+1,right)


def quick_sort(alist):
    if len(alist) <= 1:
        return alist, 0 
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
        new_less,left_count = quick_sort(less)
        new_greater, right_count = quick_sort(greater)
        left_count += len(less)
        right_count += len(greater)
        return new_less+equal+new_greater,left_count+right_count

with open("QuickSort_num.txt","r") as f:
    arr = f.read().split("\n")

print(len(arr))
_,count = quick_sort(arr)
print(count)
