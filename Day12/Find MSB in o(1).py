#method 1
from math import log
n=int(input())
print(1<<int(log(n,2)))

#method 2
def msb(n):
    n|=n>>1
    n|=n>>2
    n|=n>>4
    n|=n>>8
    n|=n>>16
    n=n+1
    return n>>1
    
