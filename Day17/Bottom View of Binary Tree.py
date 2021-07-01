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

def bottom(root):
    if not root:
        return root
    m={}
    q=[(root,0)]
    while q:
        x,v=q.pop(0)
        m[v]=x.data
        if x.left:
            q.append((x.left,v-1))
        if x.right:
            q.append((x.right,v+1))
    for i in sorted(m.keys()):
        print(m[i],end=' ')


root = node(20)
root.left = node(8)
root.right = node(22)
root.left.left = node(5)
root.left.right = node(3)
root.right.left = node(4)
root.right.right = node(25)
root.left.right.left = node(10)
root.left.right.right = node(14)

bottom(root)
