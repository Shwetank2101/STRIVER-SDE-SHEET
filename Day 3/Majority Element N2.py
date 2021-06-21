class Solution:
    def majorityElement(self, nums):
        x,count=nums[0],0
        for i in nums:
            if x==i:
                count+=1
            elif count==0:
                x,count=i,1
            else:
                count-=1
        return x
