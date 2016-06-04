import math
from time import time
import random

def fastpower(a,b):
    if b == 1:
        return a
    else:
        c = a*a
        answer = fastpower(a,math.floor(b/2))
    if b %2 != 0:
        return a*answer
    else:
        return answer

def analyze():
    wins = 0
    loses = 0
    total_diffs = []
    for _ in range(10000):
        base,power = random.randint(1,10000),random.randint(1,60)
        start = time()
        math.pow(base,power)
        builtin_pow = time() - start
        start = time()
        fastpower(base,power)
        my_pow = time()-start
        total_diffs.append(abs(my_pow - builtin_pow))
        if builtin_pow > my_pow:
            wins+=1
        else:
            loses+=1
    print("total wins",wins)
    print("total loses",loses)
    print("Average difference:",sum(total_diffs)/float(len(total_diffs)))
    print("largest difference:",max(total_diffs))
    print("min difference:", min(total_diffs))
    
analyze()
