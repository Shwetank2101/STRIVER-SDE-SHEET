def permutation(nums):
        n=len(nums)
        i=n-1
        while i>0:
            if nums[i]>nums[i-1]:
                break
            i-=1
        if i==0:
            nums.reverse()
        else:
            prev=i-1
            j=n-1
            while nums[prev]>=nums[j]:
                j-=1
            nums[prev],nums[j]=nums[j],nums[prev]
            prev=i
            j=n-1
            while prev<j:
                nums[prev],nums[j]=nums[j],nums[prev]
                prev+=1
                j-=1

