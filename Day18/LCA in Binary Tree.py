class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.val=data



def lca(root,p,q):
    if not root:
        return None
    if root.val==p or root.val==q:
        return root
    left=lca(root.left,p,q)
    right=lca(root.right,p,q)
    if left and right:
        return root
    return left or right

    


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


print(lca(root,4,5).val)
