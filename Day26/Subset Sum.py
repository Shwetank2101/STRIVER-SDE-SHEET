def subset(l,s,n):
    if s==0:
        return True
    if n==0:
        return False
    return subset(l,s-l[n-1],n-1) or subset(l,s,n-1)



def check(subset,amount):
    dp=[True]+[0]*amount
    print(dp)
    for i in subset:
        for j in range(amount,i-1,-1):
            if j-i>=0:
                dp[j]=dp[j-i] or dp[j]
    return dp[-1]


l=list(map(int,input().split()))
sum=int(input())
print(subset(l,sum,len(l)))
print(check(l,sum))
