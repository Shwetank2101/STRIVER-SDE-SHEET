#https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short=min(strs,key=len)
        c=0
        if short=='':
            return ''
        for i,j in enumerate(short):
            for k in strs:
                if k[i]!=j:
                    c=1
                    break
            if c==1:
                break
        if not(c):
            i+=1
        return short[:i]
