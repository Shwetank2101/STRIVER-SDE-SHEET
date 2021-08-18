# DP
class Solution:
    def isSubsetSum (self, N, arr, sum):
        check=[[0 for i in range(sum+1)] for j in range(N+1)]
        for i in range(N+1):
            check[i][0]=1
        for i in range(1,sum+1):
            check[0][i]=0
        for i in range(1,N+1):
            for j in range(1,sum+1):
                if j<arr[i-1]:
                    check[i][j]=check[i-1][j]
                else:
                    check[i][j]=( check[i-1][j] or  check[i-1][j-arr[i-1]])
        return check[-1][-1]


# Recursion
def check(l,x,n):
    if x<0 or n<0:
        return False
    if x==0:
        return True
    return check(l,x-l[n-1],n-1) or check(l,x,n-1)
l=list(map(int,input().split()))
x=int(input())
print(check(l,x,len(l)))

