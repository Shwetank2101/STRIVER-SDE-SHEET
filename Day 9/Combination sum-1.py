class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(l,target,out,curr):
            if target<0:
                return
            if target==0:
                out.append(curr)
                return
            for i in range(len(l)):
                dfs(l[i:],target-l[i],out,curr+[l[i]])
        out=[]
        l=candidates
        dfs(l,target,out,[])
        return out
