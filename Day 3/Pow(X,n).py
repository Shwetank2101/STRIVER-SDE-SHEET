#Recursion
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            n=-n
            x=1/x
        if n%2:
            return x*self.myPow(x*x,n//2)
        else:
            return self.myPow(x*x,n//2)

#Iteration
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            n=-n
            x=1/x
        res=1
        while n:
            if n&1:
                res=res*x
            n=n>>1
            x=x*x
        return res
