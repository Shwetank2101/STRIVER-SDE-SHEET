class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        d={}
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j] in d:
                    d[nums[i]+nums[j]].append((i,j))
                else:
                    d[nums[i]+nums[j]]=[(i,j)]
        out=set()
        for x in d:
            y=target-x
            if y in d:
                l1=d[x]
                l2=d[y]
                for i,j in l1:
                    for k,l in l2:
                        if i!=k and i!=l and j!=k and j!=l:
                            out.add(tuple(sorted([nums[i],nums[j],nums[k],nums[l]])))
        return out
            
            
