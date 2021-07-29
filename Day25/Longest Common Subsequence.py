#O(2**(n+m))
def lcs(s1,s2,m,n):
    if m==0 or n==0:
        return 0
    if s1[m-1]==s2[n-1]:
        return 1+lcs(s1,s2,m-1,n-1)
    return max(lcs(s1,s2,m,n-1),lcs(s1,s2,m-1,n))


#O(n*m)
def lcss(s1,s2):
    m=len(s1)
    n=len(s2)
    l=[[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                l[i][j]=0
            elif s1[i-1]==s2[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    x= l[m][n]
    print(x)
    res=['']*(x)
    i=m
    j=n
    while i>0 and j>0:
        if s1[i-1]==s2[j-1]:
            res[x-1]=s1[i-1]
            i-=1
            j-=1
            x-=1
        elif l[i-1][j]>l[i][j-1]:
            i-=1
        else:
            j-=1
    print(''.join(res))
    
