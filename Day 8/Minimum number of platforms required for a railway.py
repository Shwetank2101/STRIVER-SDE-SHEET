def check(a,d,n):
    a.sort()
    d.sort()
    i,j,m,p=0,0,0,1
    while i<len(a) and j<len(d):
        if a[i]<=d[j]:
            i+=1
            m+=1
        else:
            j+=1
            m-=1
        p=max(m,p)
    return p
