#By using dp
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for i in range(n)] for i in range(m)]
        print(dp)
        def count(i,j,m,n):
            if i==m-1 and j==n-1:
                return 1
            if i>=m or j>=n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]=count(i+1,j,m,n)+count(i,j+1,m,n)
            return dp[i][j]
        
        return count(0,0,m,n)

#Recursion
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def count(i,j,m,n):
            if i==m-1 and j==n-1:
                return 1
            if i>=m or j>=n:
                return 0
            return count(i+1,j,m,n)+count(i,j+1,m,n)
        return count(0,0,m,n)
# O(n*m) space
class Solution
    def uniquePaths(self, m, n):
        aux = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j-1]+aux[i-1][j]
        return aux[-1][-1]
# O(n) space 
def uniquePaths(self, m, n):
    if not m or not n:
        return 0
    cur = [1] * n
    for i in xrange(1, m):
        for j in xrange(1, n):
            cur[j] += cur[j-1]
    return cur[-1]
