class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def bfs(k,l,path,out):
            out.append(path)
            for i in range(k,len(l)):
                if i>0 and l[i]==l[i-1]:
                    continue
                bfs(i+1,l,path+[l[i]],out)
        out=[]
        bfs(0,nums,[],out)
        return out
