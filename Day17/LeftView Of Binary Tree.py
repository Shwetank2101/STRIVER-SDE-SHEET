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

 

#using queue     
def levelOrder(root):
    if not root:
        return None
    q=[root]
    while q:
        for i in range(len(q)):
            x=q.pop(0)
            if i==0:
                print(x.data,end=' ')
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)

#using recursion

def leftview(root,level,max_level):
    if root==None:
        return
    if max_level[0]<level:
        print(root.data,end=' ')
        max_level[0]=level
    leftview(root.left,level+1,max_level)
    leftview(root.right,level+1,max_level)
    
    

root=node(4)
root.left=node(5)
root.right=node(2)
root.right.left=node(3)
root.right.right=node(1)
root.right.left.left=node(6)
root.right.left.right=node(7)


levelOrder(root)
print()
leftview(root,1,[0])


