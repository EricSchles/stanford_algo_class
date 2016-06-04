import math

def decompose(integer,mid):
    string_version = str(integer)
    a = int(string_version[:mid])
    b = int(string_version[mid:])
    return a,b

def multiply(first,second):
    size_of_first = len(str(first))
    size_of_second = len(str(second))
    if  size_of_first == 1 or size_of_second == 1:
        return first*second
    else:
        exp = min(int(math.ceil(size_of_first/2)),int(math.ceil(size_of_second/2)))
        a,b = decompose(first,size_of_first-exp)
        c,d = decompose(second,size_of_second-exp)
        return (math.pow(10,exp*2) * multiply(a,c)) + math.pow(10,exp) * (multiply(a,d)+multiply(b,c)) + multiply(b,d)
        
assert 50*50 == multiply(50,50)
