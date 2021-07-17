#https://leetcode.com/problems/coin-change/submissions/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf=float('inf')
        dp=[0]+[inf]*amount
        for i in range(1,amount+1):
            for j in coins:
                if i-j>=0:
                    dp[i]=min(dp[i-j],dp[i])
            dp[i]+=1
        if dp[-1]!=inf:
            return dp[-1]
        return -1

#https://leetcode.com/problems/coin-change-2/submissions/
def count(coins,amount):
    dp=[1]+[0]*amount
    print(dp)
    for i in coins:
        for j in range(1,amount+1):
            if j-i>=0:
                dp[j]+=dp[j-i]
        print(dp)
    return dp[-1]





