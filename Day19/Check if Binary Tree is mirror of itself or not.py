class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.val=data

def checkmirror(root1,root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val==root2.val:
        return (checkmirror(root1.left,root2.right) and checkmirror(root1.left,root2.right))

root1 = Node(1)
root2 = Node(1)
 
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
 
root2.left = Node(3)
root2.right = Node(2)
root2.right.left = Node(5)
root2.right.right = Node(4)
print(checkmirror(root1,root2))
