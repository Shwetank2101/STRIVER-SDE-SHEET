class Solution:
    def maxProfit(self, l: List[int]) -> int:
        m,q=0,0
        for i in range(1,len(l)):
            q=max(0,l[i]-l[i-1]+q)
            m=max(m,q)
        return (m)

        
