class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n//2):
            for j in range(n):
                matrix[j][i],matrix[j][n-i-1]=matrix[j][n-i-1],matrix[j][i]
        
        
