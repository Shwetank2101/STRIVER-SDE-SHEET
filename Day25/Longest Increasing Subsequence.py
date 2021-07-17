#https://leetcode.com/problems/longest-increasing-subsequence/submissions/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        for i in range(1,n):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
