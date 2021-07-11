#Brute Force
def check(s):
    if s[::-1]==s:
        return True
    else:
        return False
def palindrome(s):
    n=len(s)
    c=1
    out=s[0]
    for i in range(n,1,-1):
        for j in range(0,n-i+1):
            if check(s[j:j+i]):
                c=i
                out=s[j:j+i]
                break
        if c!=1:
            break
    print(c,out)

#Dp
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        l=[[0 for i in range(n)] for j in range(n)]
        a=s[0]
        c=1
        for i in range(n):
            l[i][i]=1
        for i in range(n-1):
            if s[i]==s[i+1]:
                if c<2:
                    a=s[i:i+2]
                    c=2
                l[i][i+1]=1
        for i in range(2,n):
            for j in range(n-i):
                if s[j]==s[j+i] and l[j+1][j+i-1]:
                    if i+1>c:
                        c=i+1
                        a=s[j:j+i+1]
                    l[j][j+i]=1
        return a

#
