class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n==0:
            return 
        i,j=0,0
        while i<m:
            if nums2[j]<nums1[i]:
                nums2[j],nums1[i]=nums1[i],nums2[j]
                for k in range(j,n):
                    if nums2[j]>nums2[k]:
                        nums2[j],nums2[k]=nums2[k],nums2[j]
            i+=1
        for i in range(n):
            nums1[m+i]=nums2[i]
        
        
