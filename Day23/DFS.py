def dfsutil(d,x,visited):
    visited.add(x)
    print(x,end=' ')
    for i in d[x]:
        if i not in visited:
            dfsutil(d,i,visited)
def dfs(d,x):
    visited=set()
    dfsutil(d,x,visited)
    print()
