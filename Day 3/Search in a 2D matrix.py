#O(nlog(m))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarysearch(l,i,j,x):
            if i<=j:
                mid=(i+j)//2
                if l[mid]>x:
                    return binarysearch(l,i,mid-1,x)
                elif l[mid]<x:
                    return binarysearch(l,mid+1,j,x)
                else:
                    return True
            return False
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            if binarysearch(matrix[i],0,m-1,target):
                return True
        else:
            return False

#O(max(m,n))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        i,j=0,m-1
        while i<n and j>=0:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                j-=1
            else:
                i+=1
        return False
        
                
