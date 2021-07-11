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
def construct(start,end,preorder,inorder,curr):
    if start>end:
        return
    node=Node(preorder[curr[0]])
    curr[0]+=1
    x=search(node.val,inorder,start,end)
    node.left= construct(start,x-1,preorder,inorder,curr)
    node.right= construct(x+1,end,preorder,inorder,curr)
    return node

#O(n)
def constructn(start,end,preorder,inorder,curr,d):
    if start>end:
        return
    node=Node(preorder[curr[0]])
    curr[0]+=1
    x=d[node.val]
    node.left= constructn(start,x-1,preorder,inorder,curr,d)
    node.right= constructn(x+1,end,preorder,inorder,curr,d)
    return node

def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print(node.val,end=' ')
    printInorder(node.right)
  
inorder = ['D', 'B', 'E', 'A', 'F', 'C']
preorder = ['A', 'B', 'D', 'E', 'C', 'F']
curr=[0]
root=construct(0,len(inorder)-1,preorder,inorder,curr)
printInorder(root)
print()
d={}
for i in range(len(inorder)):
    d[inorder[i]]=i
curr=[0]
root=constructn(0,len(inorder)-1,preorder,inorder,curr,d)
printInorder(root)
print()
