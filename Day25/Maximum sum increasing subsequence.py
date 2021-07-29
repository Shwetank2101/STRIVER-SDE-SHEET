def maxum(nums):
        n=len(nums)
        dp=[nums[0]]+[0]*n
        for i in range(1,n):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+nums[i])
        return max(dp)
