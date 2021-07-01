from collections import defaultdict as df
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        m=0
        l=0
        d={}
        for i in range(n):
            if s[i] in d and d[s[i]]>=l:
                l=d[s[i]]+1
            else:
                m=max(m,i-l+1)
            d[s[i]]=i
        return m
