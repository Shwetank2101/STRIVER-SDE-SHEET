#O(3**n)
def edit(s1,s2,m,n):
    if m==0:
        return n
    if n==0:
        return m
    if s1[m-1]==s2[n-1]:
        return edit(s1,s2,m-1,n-1)
    return 1+min(edit(s1,s2,m,n-1),edit(s1,s2,m-1,n-1),edit(s1,s2,m-1,n))

    
    
#O(n*m)
def editt(s1,s2,m,n):
    if m==0:
        return n
    if n==0:
        return m
    dp=[[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            elif s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])
    return dp[m][n]
