import math
def karatsuba(x,y):
    len_x,len_y = len(str(x)),len(str(y))
    if len_x == 1 or len_y == 1:
        return x*y
    else:
        exp = min(int(math.ceil(len_x/2)),int(math.ceil(len_y/2)))
        mid_x = len_x-exp
        mid_y = len_y-exp
        a,b = str(x)[:mid_x],str(x)[mid_x:]
        a,b = int(a),int(b)
        c,d = str(y)[:mid_y],str(y)[mid_y:]
        c,d = int(c),int(d)
        first_term = karatsuba(a,c)
        third_term = karatsuba(b,d)
        second_term = karatsuba(a+b,c+d) - first_term - third_term
        return math.pow(10,2*exp)*first_term + math.pow(10,exp)*second_term + third_term

multiply = karatsuba
assert 50*50 == multiply(50,50)
assert 25*25 == multiply(25,25)
assert 1151*1151 == multiply(1151,1151)
assert 251*251 == multiply(251,251)
assert 151*202 == multiply(151,202)

