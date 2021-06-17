class Solution:
    def addTwoNumbers(self, root1: ListNode, root2: ListNode) -> ListNode:
        first=root1
        second=root2
        carry=0
        root=temp=node(0)
        while first or second:
            v1,v2=0,0
            if first:
                v1=first.data
                first=first.next
            if second:
                v2=second.data
                second=second.next
            sum1=v1+v2+carry
            if sum1>=10:
                carry=1
                sum1%=10
            else:
                carry=0
            temp.next=node(sum1)
            temp=temp.next
        if carry:
            temp.next=node(carry)
        return root.next
