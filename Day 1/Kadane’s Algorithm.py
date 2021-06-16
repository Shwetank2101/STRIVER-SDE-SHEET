def sum(l):
    n=len(l)
    s=0
    c=l[0]
    for i in range(1,n):
        if c+l[i]>0:
            c+=l[i]
        else:
            c=0
        s=max(c,s)
    print(s)
            
