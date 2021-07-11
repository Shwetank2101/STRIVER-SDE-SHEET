class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.val=data


def search(x,nums,start,end):
    for i in range(start,end+1):
        if nums[i]==x:
            return i
#O(n**2)    
def construct(start,end,postorder,inorder,curr):
    if start>end:
        return
    node=Node(postorder[curr[0]])
    curr[0]-=1
    x=search(node.val,inorder,start,end)
    node.right= construct(x+1,end,postorder,inorder,curr)
    node.left= construct(start,x-1,postorder,inorder,curr)
    return node

#O(n)
def constructn(start,end,postorder,inorder,curr,d):
    if start>end:
        return
    node=Node(postorder[curr[0]])
    curr[0]-=1
    x=d[node.val]
    node.right= constructn(x+1,end,postorder,inorder,curr,d)
    node.left= constructn(start,x-1,postorder,inorder,curr,d)
    return node


def printpreorder(node):
    if node:
        print(node.val,end=' ')
        printpreorder(node.left)
        printpreorder(node.right)
  
inorder = [4, 8, 2, 5, 1, 6, 3, 7]
postorder = [8, 4, 5, 2, 6, 7, 3, 1]
n=len(inorder)
curr=[n-1]
root=construct(0,n-1,postorder,inorder,curr)
printpreorder(root)
print()
d={}
for i in range(n):
    d[inorder[i]]=i
curr=[n-1]
root=constructn(0,n-1,postorder,inorder,curr,d)
printpreorder(root)
print()
