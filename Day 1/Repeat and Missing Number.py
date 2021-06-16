class Solution:
    def missing(self, nums):
        n=len(nums)
        x=0
        for i in range(n):
            x=x^nums[i]^(i+1)
        a,b=0,0
        x=x& ~(x-1)
        for i in range(n):
            if x&nums[i]:
                a=a^nums[i]
            else:
                b=b^nums[i]
            if x&(i+1):
                a=a^(i+1)
            else:
                b=b^(i+1)
        print(a,b)
        
