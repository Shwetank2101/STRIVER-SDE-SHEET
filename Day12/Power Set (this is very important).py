l=list(map(int,input().split()))
n=len(l)
size=1<<n
t=[]
for i in range(size):
    for j in range(n):
        if i&(1<<j)!=0:
            print(l[j],end=' ')
    print()
