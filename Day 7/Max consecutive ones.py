class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s,m=0,0
        for i in nums:
            if i==0:
                s=0
            else:
                s+=1
            m=max(s,m)
        return m
