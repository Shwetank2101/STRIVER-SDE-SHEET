#O(n) space
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        su=[0]*n
        pre=[0]*n
        m=0
        for i in range(n):
            m=max(height[i],m)
            pre[i]=m
        m=0
        for i in range(n-1,-1,-1):
            m=max(height[i],m)
            su[i]=m
        count=0
        for i in range(n):
            count+=min(pre[i],su[i])-height[i]
        return count

#O(1) space
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        count,leftmax,rightmax,i,j=0,0,0,0,n-1
        while i<=j:
            if height[i]<height[j]:
                if height[i]>leftmax:
                    leftmax=height[i]
                else:
                    count+=leftmax-height[i]
                i+=1
            else:
                if height[j]>rightmax:
                    rightmax=height[j]
                else:
                    count+=rightmax-height[j]
                j-=1
        return count
            
        
