#Unique elements
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permute(s,answer,c):
            if len(s)==0:
                answer.append(c)
                return
            for i in range(len(s)):
                permute(s[:i]+s[i+1:],answer,c+[s[i]])
        answer=[]
        permute(nums,answer,[])
        return answer


#Not unique elements
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permute(s,answer,c):
            if len(s)==0:
                answer.append(c)
                return
            for i in range(len(s)):
                if i>0 and s[i]==s[i-1]:
                    continue
                permute(s[:i]+s[i+1:],answer,c+[s[i]])
        answer=[]
        nums.sort()
        permute(nums,answer,[])
        return answer
