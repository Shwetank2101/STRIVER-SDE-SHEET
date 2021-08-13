# O(2**n)
def rod(price,n):
    if n<=0:
        return 0
    max_val=-1
    for i in range(n):
        max_val=max(max_val,price[i]+rod(price,n-i-1))
    return max_val


def rodd(price,n,val):
    if n<=0:
        return 0
    if val[n]:
        return val[n]
    max_val=-1
    for i in range(n):
        max_val=max(max_val,price[i]+rodd(price,n-i-1,val))
    val[n]=max_val
    return max_val


# O(n**2)
def cutrod(price,n):
    val=[0]*(n+1)
    for i in range(1,n+1):
        maxi=-1
        for j in range(i):
            maxi=max(maxi,price[j]+val[i-j-1])
        val[i]=maxi
    return val[n]


