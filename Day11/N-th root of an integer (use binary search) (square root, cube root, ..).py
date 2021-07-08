def power(x,n):
    if x>=0 and x<1:
        low=x
        high=1
    else:
        low=1
        high=x
    correction=10**(-6)
    mid=(low+high)/2
    
    while abs(mid**n-x)>=correction:
        if mid**n>x:
            high=mid
        else:
            low=mid
        mid=(high+low)/2
    print(mid)
for i in range(int(input())):
    n,m=map(float,input().split())
    power(n,m)
