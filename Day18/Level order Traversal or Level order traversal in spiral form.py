class newNode:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def levelspiral(root):
    if not root:
        return root
    curr=[root]
    next=[]
    temp=False
    while curr:
        x=curr.pop(-1)
        print(x.data,end=' ')
        if temp:
            if x.left:
                next.append(x.left)
            if x.right:
                next.append(x.right)
        else:
            if x.right:
                next.append(x.right)
            if x.left:
                next.append(x.left)
        if not curr:
            temp=not temp
            next,curr=curr,next

root = newNode(1) 
root.left = newNode(2) 
root.right = newNode(3) 
root.left.left = newNode(7) 
root.left.right = newNode(6) 
root.right.left = newNode(5) 
root.right.right = newNode(4) 
levelspiral(root)
        
        
