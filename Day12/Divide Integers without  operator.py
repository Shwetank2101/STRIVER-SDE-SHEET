def check(divident,divisor):
    curr=0
    res=0
    for i in range(31,0,-1):
        if curr+(divisor<<i)<=divident:
            curr+=divisor<<i
            res=res | (1<<i)
    return res
