def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    else:
        mid = len(alist)//2 
        return merge(merge_sort(alist[:mid]),merge_sort(alist[mid:]))

def merge(left,right):
    left_p,right_p = 0,0
    merged = []
    while len(left) > left_p and len(right) > right_p:
        if left[left_p] < right[right_p]:
            merged.append(left[left_p])
            left_p += 1
        else:
            merged.append(right[right_p])
            right_p += 1
    while len(left) > left_p:
        merged.append(left[left_p])
        left_p += 1
    while len(right) > right_p:
        merged.append(right[right_p])
        right_p += 1
    return merged

print(merge_sort([1,4,4,3,2]))
