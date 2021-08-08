class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path=[]
        result=[]
        self.dfs(path,result,s)
        return result
    def dfs(self,path,result,s):
        if not s:
            result.append(path)
            return
        for i in range(1,len(s)+1):
            if self.palindrome(s[:i]):
                self.dfs(path+[s[:i]],result,s[i:])
    def palindrome(self,s):
        return s[::-1]==s
