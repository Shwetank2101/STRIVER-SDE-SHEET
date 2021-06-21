class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        j=0
        for i in range(1,n):
            if nums[i]!=nums[j]:
                j+=1
                nums[i],nums[j]=nums[j],nums[i]
        return j+1
            
                    
