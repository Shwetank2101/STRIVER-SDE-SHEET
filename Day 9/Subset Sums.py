def check(l,x,n):
    if x<0 or n<0:
        return False
    if x==0:
        return True
    return check(l,x-l[n-1],n-1) or check(l,x,n-1)
l=list(map(int,input().split()))
x=int(input())
print(check(l,x,len(l)))
