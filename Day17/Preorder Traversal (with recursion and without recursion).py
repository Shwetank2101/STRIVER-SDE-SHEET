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

#Recursion            
def preorderr(root):
    if root:
        print(root.data,end=' ')
        preorderr(root.left)
        preorderr(root.right)


#Interative
def preorder(root):
    temp=root
    stack=[]
    while True:
        if temp:
            print(temp.data,end=' ')
            stack.append(temp)
            temp=temp.left
        elif stack:
            temp=stack.pop()
            temp=temp.right
        else:
            break


root=node(5)
push(root,5)
push(root,6)
push(root,7)
push(root,8)
preorder(root)
print()
preorderr(root)



