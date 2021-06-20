class Node():
    def __init__(self,data):
        self.val = data
        self.next = None
        self.down=None
def push(root,data):
    new=Node(data)
    new.down=root
    root=new
    return root
def printList(root):
    temp=root
    while temp:
        print(temp.val,end=' ')
        temp=temp.down
    print()
    
def printList1(root):
    temp=root
    while temp:
        print(temp.val,end=' ')
        temp=temp.next
    print()

def merge(a,b):
    if a==None:
        return b
    if b==None:
        return a
    result=None
    if a.val<=b.val:
        result=Node(a.val)
        result.down=merge(a.down,b)
    else:
        result=Node(b.val)
        result.down=merge(a,b.down)
    result.next=None
    return result
def flatten(root):
    if root==None or root.next==None:
        return root
    root.next=flatten(root.next)
    root=merge(root,root.next)
    return root
'''
Let us create the following linked list
            5 -> 10 -> 19 -> 28
            |    |     |     |
            V    V     V     V
            7    20    22    35
            |          |     |
            V          V     V
            8          50    40
            |                |
            V                V
            30               45
'''
root=Node(30)
root=push(root,8)
root=push(root,7)
root=push(root,5)
root.next=Node(20)
root.next=push(root.next,10)
root.next.next=Node(50)
root.next.next=push(root.next.next,22)
root.next.next=push(root.next.next,19)
root.next.next.next=Node(45)
root.next.next.next=push(root.next.next.next,40)
root.next.next.next=push(root.next.next.next,35)
root.next.next.next=push(root.next.next.next,28)
root=flatten(root)

printList(root)


