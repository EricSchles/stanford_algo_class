def merge_sort(alist):
   if len(alist) > 1:
      mid = len(alist)//2
      right, right_count = merge_sort(alist[:mid])
      left, left_count = merge_sort(alist[mid:])
      merged, merge_count = merge(left,right)
      return merged, merge_count+left_count+right_count
   else:
      return alist, 0

def merge(left,right):
   count = 0
   merged = []
   while left and right:
      if left[0] <= right[0]: 
         merged.append(left.pop(0)) 
      else: 
          count += len(left)
          merged.append(right.pop(0)) 
   merged  += left + right     
   return merged, count
