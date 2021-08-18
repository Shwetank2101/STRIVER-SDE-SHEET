from sys import maxsize
# Exponential complexity
def egg(n,k):
    if n==1 or k==1 or k==0:
        return k
    mini=maxsize
    for i in range(1,k+1):
        mini=min(mini,max(egg(n-1,i-1),egg(n,k-i)))
    return mini+1


