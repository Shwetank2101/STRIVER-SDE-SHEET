from collections import defaultdict as df
def bfs(d,x):
    visited,q=set(),[]
    q.append(x)
    visited.add(x)
    while q:
        s=q.pop(0)
        print(s,end=' ')
        for i in d[s]:
            if i not in visited:
                q.append(i)
                visited.add(i)
    print()
    
