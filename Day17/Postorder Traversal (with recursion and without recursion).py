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
def postorderr(root):
    if root:
        postorderr(root.left)
        postorderr(root.right)
        print(root.data,end=' ')

#Iterative 2 stack
def postorder1(root):
        out, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                out.append(node.data)
                stack.append(node.left)
                stack.append(node.right)

        return out[::-1]

#Iterative 1 stack
def postorder2(root):
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    print(node.data,end=' ')
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))


root=node(1)
push(root,2)
push(root,3)
push(root,4)
push(root,5)
push(root,6)
push(root,7)
push(root,8)

postorderr(root)
print()
print(*postorder1(root))
postorder2(root)



