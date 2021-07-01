class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def push(root,data):
    if root==None:
        root=node(data)
        return
    q=[root]
    while True:
        x=q.pop(0)
        if x.left==None:
            x.left=node(data)
            break
        else:
            q.append(x.left)
        if x.right==None:
            x.right=node(data)
            break
        else:
            q.append(x.right)

def top(root):
    if not root:
        return root
    m={}
    q=[(root,0)]
    while q:
        x,v=q.pop(0)
        if v not in m:
            m[v]=x.data
        if x.left:
            q.append((x.left,v-1))
        if x.right:
            q.append((x.right,v+1))
    for i in sorted(m.keys()):
        print(m[i],end=' ')


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.right = node(4)
root.left.right.right = node(5)
root.left.right.right.right = node(6)

top(root)
