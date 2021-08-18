class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(l,target,out,curr):
            if target<0:
                return
            if target==0:
                out.append(curr)
                return
            for i in range(1,len(l)+1):
                if i>1 and l[i-1]==l[i-2]:
                    continue
                dfs(l[i:],target-l[i-1],out,curr+[l[i-1]])
        out=[]
        l=candidates
        l.sort()
        dfs(l,target,out,[])
        return out
