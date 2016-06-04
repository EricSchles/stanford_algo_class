import random

def r_select(alist,len_alist,ith_order_statistic):
    if len(alist) <= 1:
        return alist[0]
    else:
        pivot = random.randint(0,len(alist)-1)
        new_index = partition(alist,0,len(alist)-1,alist[pivot])
        if new_index == ith_order_statistic:
            return alist[pivot]
        elif new_index > ith_order_statistic:
            return r_select(alist[:new_index],new_index-1,ith_order_statistic)
        elif new_index < ith_order_statistic:
            return r_select(alist[new_index:],len_alist-new_index,ith_order_statistic-new_index)
        
def partition(alist,first,last,pivotvalue):
    leftmark = first+1
    rightmark = last
    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark

listing = [0,1,2,3]
print(r_select(listing,len(listing),2))
