#Cycle method
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x=nums[0]
        y=nums[0]
        while(True):
            x=nums[x]
            y=nums[nums[y]]
            print(x,y)
            if x==y:
                break
        x=nums[0]
        while x!=y:
            x=nums[x]
            y=nums[y]
        else:
            return x

#Visited array
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            c=abs(nums[i])
            if nums[c]>=0:
                nums[c]=-nums[c]
            else:
                return abs(nums[i])
        
