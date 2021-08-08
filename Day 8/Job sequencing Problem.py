def job(l):
    l.sort(key=lambda x:x[-1],reverse=True)
    n=len(l)
    m=0
    for i in range(n):
        m=max(m,l[i][1])
    check=[0]*m
    for i in range(n):
        for j in range(l[i][1]-1,-1,-1):
            if check[j]==0:
                check[j]=l[i][0]
                break
    for i in range(m):
        if check[i]!=0:
            print(check[i],end=' ')
    
l=[]
for i in range(int(input())):
    l.append(list(map(str,input().split())))
    l[i][-1]=int(l[i][-1])
    l[i][-2]=int(l[i][-2])
job(l)
