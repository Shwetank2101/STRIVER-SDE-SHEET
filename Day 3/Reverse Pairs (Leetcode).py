class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(nums,temp,left,right,mid):
            count=0
            j=mid+1
            
            for i in range(left,mid+1):
                while j<=right and nums[i]>2*nums[j]:
                    j+=1
                count+=(j-mid-1)
            i=left
            j=mid+1
            k=left
            while i<=mid and j<=right:
                if nums[i]<nums[j]:
                    temp[k]=nums[i]
                    i+=1
                else:
                    temp[k]=nums[j]
                    j+=1
                k+=1
            while i<=mid:
                temp[k]=nums[i]
                k+=1
                i+=1
            while j<=right:
                temp[k]=nums[j]
                k+=1
                j+=1
            for i in range(left,right+1):
                nums[i]=temp[i]
            
            return count
        def mergesort(nums,temp,left,right):
            inv=0
            if left<right:
                mid=(left+right)//2
                inv+=mergesort(nums,temp,left,mid)
                inv+=mergesort(nums,temp,mid+1,right)
                inv+=merge(nums,temp,left,right,mid)
            return inv
        n=len(nums)
        temp=[0]*(n)
        return mergesort(nums,temp,0,n-1)
                
            
        
