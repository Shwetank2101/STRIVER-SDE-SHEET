def maxpath(mat):
    n=len(mat)
    m=len(mat[0])
    for i in range(n-1,0,-1):
        for j in range(m):
            if j>0 and j<m-1:
                mat[i-1][j]=mat[i-1][j]+max(mat[i][j],mat[i][j-1],mat[i][j+1])
            elif j>1:
                mat[i-1][j]=mat[i-1][j]+max(mat[i][j],mat[i][j-1])
            else:
                mat[i-1][j]=mat[i-1][j]+mat[i][j]
    mi=0
    for i in range(m):
        mi=max(mat[0][i],mi)
    print(mi)

mat=[]
for i in range(int(input())):
    mat.append(list(map(int,input().split())))
maxpath(mat)
            
