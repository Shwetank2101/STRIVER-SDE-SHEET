class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i,m,j=0,0,len(nums)-1
        while m<=j:
            if nums[m]==0:
                nums[m],nums[i]=nums[i],nums[m]
                m+=1
                i+=1
            elif nums[m]==1:
                m+=1
            elif nums[m]==2:
                nums[m],nums[j]=nums[j],nums[m]
                j-=1
