#O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={}
        m=0
        for i in nums:
            d[i]=1
        for i in nums:
            if i-1 not in d:
                j=i
                while j in d:
                    j+=1
                m=max(j-i,m)
        return m

#O(n*log(n))
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=list(set(nums))
        nums.sort()
        
        m=1
        c=0
        for i in range(1,len(nums)):
            if nums[i-1]+1==nums[i]:
                m+=1
            else:
                c=max(c,m)
                m=1
        c=max(c,m)
        return c
