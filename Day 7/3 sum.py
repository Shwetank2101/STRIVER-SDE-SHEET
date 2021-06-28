from collections import defaultdict as df
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        out=[]
        for i in range(n-2):
            if i==0 or nums[i]!=nums[i-1]:
                low=i+1
                high=n-1
                sum=-nums[i]
                while low<high:
                    if nums[low]+nums[high]==sum:
                        out.append([nums[low],nums[high],nums[i]])
                        while low<high and nums[low]==nums[low+1]:
                            low+=1
                        while low<high and nums[high]==nums[high-1]:
                            high-=1
                        low-=1
                        high-=1
                    elif nums[low]+nums[high]>sum:
                        high-=1
                    else:
                        low+=1
        return out
            
                    
                
            
        
            
