class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ma=nums[0]
        mi=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            choice1=ma*nums[i]
            choice2=mi*nums[i]
            ma=max(choice1,choice2,nums[i])
            mi=min(choice1,choice2,nums[i])
            ans=max(ans,ma)
        return ans
            
