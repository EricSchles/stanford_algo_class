from numba import jit
with open("IntegerArray.txt","r") as f:
    arr = [int(elem) for elem in f.read().split("\n") if elem !='']

@jit
def get_inv_count(arr):
    count = 0
    for ind,i in enumerate(arr):
        for j in arr[ind:]:
            if i > j:
                count += 1
    return count

def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        left, left_count = merge_sort(alist[:mid])
        right, right_count = merge_sort(alist[mid:])
        merged, merge_count = merge(left,right)
        return merged, merge_count+left_count+right_count
    else:
        return alist, 0

def merge(left,right):
    left_p,right_p = 0,0    
    count = 0
    merged = []
    while len(left) > left_p and len(right) > right_p:
        if left[left_p] <= right[right_p]: 
            merged.append(left[left_p])
            left_p += 1
        else: 
            count += len(left) - left_p
            merged.append(right[right_p])
            right_p += 1

    while left_p < len(left):
        merged.append(left[left_p])
        left_p += 1
    while right_p < len(right):
        merged.append(right[right_p])
        right_p += 1
    return merged, count

_,count = merge_sort(arr)
print(count)
_,count = SortCount(arr)
print(count)
