class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k-=1
        out=''
        num=[i for i in range(1,n+1)]
        while n:
            n-=1
            q,k=divmod(k,math.factorial(n))
            out+=str(num[q])
            num.remove(num[q])
        return out
            
        
