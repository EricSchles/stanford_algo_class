#this is wrong, presently
def quicksort(alist,start,end):
    if start < end:
        pivot = partition(alist,0,len(alist))
        quicksort(alist,start,pivot-1)
        quicksort(alist,pivot+1,end)
        return alist
        
def partition(alist,l,r):
    p = alist[l]
    i = l+1
    for j in range(l+1,r):
        if alist[j] < p:
            alist[j],alist[i] = alist[i],alist[j]
            i += 1
    alist[l],alist[i-1] = alist[i-1],alist[l]
    return i

listing = [4,3,2,1]
print(quicksort(listing,0,len(listing)))
