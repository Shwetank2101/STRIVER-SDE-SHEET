#O(n+m) space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix[0])
        n=len(matrix)
        row=[1]*n
        col=[1]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row[i]=0
                    col[j]=0
        for i in range(n):
            if row[i]==0:
                for j in range(m):
                    matrix[i][j]=0
        for i in range(m):
            if col[i]==0:
                for j in range(n):
                    matrix[j][i]=0

#O(1) space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix[0])
        n=len(matrix)
        x=0
        for i in range(n):
            if matrix[i][0]==0:
                x=1
            for j in range(1,m):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(n-1,-1,-1):
            for j in range(m-1,0,-1):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
            if x:
                matrix[i][0]=0
                    
