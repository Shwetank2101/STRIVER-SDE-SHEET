def total(x):
    if x==1 or x==0:
        return x
    res=0
    c=count(x)
    res+=(1<<(c-1))*c
    res+=(x-(1<<(c))+1)+total(x-(1<<c))
    return res
def count(x):
    c=0
    while 1<<c <=x:
        c+=1
    return c-1
n=int(input())
print(total(n))
