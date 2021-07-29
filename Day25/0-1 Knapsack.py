#O(2**n)
def knapsack(am,wt,val,n):
    if n==0 or am==0:
        return 0
    if am<wt[n-1]:
        return knapsack(am,wt,val,n-1)
    else:
        return max(val[n-1]+knapsack(am-wt[n-1],wt,val,n-1),knapsack(am,wt,val,n-1))
    
#(n**2)
def knapsackk(am,wt,val,n):
    dp=[[0]*(am+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(am+1):
            if i==0 or j==0:
                continue
            elif j>=wt[i-1]:
                dp[i][j]=max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][am]
            
