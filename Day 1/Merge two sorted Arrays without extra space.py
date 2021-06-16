# O(n*m) time,  O(1) space
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n==0:
            return 
        i,j=0,0
        while i<m:
            if nums2[j]<nums1[i]:
                nums2[j],nums1[i]=nums1[i],nums2[j]
                while(j<n-1 and nums2[j]>nums2[j+1]):
                    nums2[j],nums2[j+1]=nums2[j+1],nums2[j]
                    j+=1
                j=0
                    
            i+=1
        for i in range(n):
            nums1[m+i]=nums2[i]


# O(log(n+m)) time,  O(1) space
import math
def gapf(n):
    if n==1:
        return 0
    return math.ceil(n/2)
def sort(l1,l2):
    n=len(l1)
    m=len(l2)
    gap=n+m
    gap=gapf(gap)
    while gap>0:
        i=0
        while i+gap<n:
            if l1[i]>l1[i+gap]:
                l1[i],l1[i+gap]=l1[i+gap],l1[i]
            i+=1
        j=gap-n if gap>n else 0
        while i<n and j<m:
            if l1[i]>l2[j]:
                l1[i],l2[j]=l2[j],l1[i]
            i+=1
            j+=1
        if j<m:
            j=0
            while j+gap<m:
                if l2[j]>l2[j+gap]:
                    l2[j],l2[j+gap]=l2[j+gap],l2[j]
                j+=1
        gap=gapf(gap)
        
    
