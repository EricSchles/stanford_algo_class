from collections import namedtuple
import math
import random
Point = namedtuple("Point","x,y")

def distance(p1,p2):
    return math.sqrt( math.pow((p2.x - p1.x),2) + math.pow((p2.y - p1.y),2))

def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    else:
        mid = len(alist)//2
        left = merge_sort(alist[:mid])
        right = merge_sort(alist[mid:])
        return merge(left,right)
    
def merge(left,right):
    merged = []
    left_p,right_p = 0,0
    while len(left) > left_p and len(right) > right_p:
        if left[left_p] < right[right_p]:
            merged.append(left[left_p])
            left_p += 1
        else:
            merged.append(right[right_p])
            right_p += 1
    merged += left[left_p:] + right[right_p:]
    return merged

def find_closest_pair(ordered_by_x,ordered_by_y):
    if len(ordered_by_x) <= 3:
        distances = {}
        for i in range(len(ordered_by_x)):
            for j in range(len(ordered_by_x)):
                #distances[distance(ordered_by_x[i],ordered_by_y[j])] = (ordered_by_x[i],ordered_by_y[j])
                if i != j:
                    distances[distance(ordered_by_x[i],ordered_by_x[j])] = (ordered_by_x[i],ordered_by_x[j])
                    #distances[distance(ordered_by_y[i],ordered_by_y[j])] = (ordered_by_y[i],ordered_by_y[j])
        return distances[min(distances.keys())]
    else:
        mid = len(ordered_by_x)//2
        points = []
        points.append(list(find_closest_pair(ordered_by_x[:mid],ordered_by_y[:mid])))
        points.append(list(find_closest_pair(ordered_by_x[mid:],ordered_by_y[mid:])))
        
        distances = {}
        for point_set in points:
            distances[distance(point_set[0],point_set[1])] = point_set
        delta = min(distances.keys())
        split_case = check_split_case(ordered_by_x,ordered_by_y,delta)
        
        if split_case:
            if min(delta,distance(split_case[0],split_case[1])) == delta:
                return distances[min(distances.keys())] 
            else:
                return split_case
        else:
            return distances[min(distances.keys())]
        
def check_split_case(ordered_by_x,ordered_by_y,delta):
    x_bar = ordered_by_x[len(ordered_by_x)//2]
    x_coordinates_to_check = [elem.x for elem in ordered_by_x if elem.x < x_bar.x + delta and elem.x > x_bar.x - delta]
    coordinates = [elem for elem in ordered_by_y if elem.x in x_coordinates_to_check]
    smallest_distance = delta
    best_pair = None
    for i in range(len(coordinates)-1):
        for j in range(1,min(7,len(coordinates)-i)):
            p,q = coordinates[i],coordinates[i+j]
            if distance(p,q) < smallest_distance:
                best_pair = (p,q)
                smallest_distance = distance(p,q)
    return best_pair

def impose_ordering(coordinates,old_ordering,new_ordering):
    dicter = {}
    for ind,elem in enumerate(old_ordering):
        dicter[new_ordering.index(elem)] = ind
    new_coordinates = []
    for ind in range(len(coordinates)):
        new_coordinates.append(coordinates[dicter[ind]])
    return new_coordinates

#coordinates = [Point(i,i) for i in range(1000)]
coordinates = []
x_s = []
y_s = []
for _ in range(10000):
    tmp_x,tmp_y = random.randint(0,100000),random.randint(0,100000)
    while tmp_x in x_s or tmp_y in y_s:
        tmp_x,tmp_y = random.randint(0,100000),random.randint(0,100000)
    tmp_p = Point(tmp_x,tmp_y)
    x_s.append(tmp_x)
    y_s.append(tmp_y)
    coordinates.append(tmp_p)

old_x_ordering = [elem.x for elem in coordinates]
new_x_ordering = merge_sort([elem.x for elem in coordinates])
old_y_ordering = [elem.y for elem in coordinates]
new_y_ordering = merge_sort([elem.y for elem in coordinates])

ordered_by_x = impose_ordering(coordinates,old_x_ordering,new_x_ordering)
ordered_by_y = impose_ordering(coordinates,old_y_ordering,new_y_ordering)

pair = find_closest_pair(ordered_by_x,ordered_by_y)
print("Point 1:",pair[0].x,pair[0].y)
print("Point 2:",pair[1].x,pair[1].y)
print("Distance:",distance(pair[0],pair[1]))
