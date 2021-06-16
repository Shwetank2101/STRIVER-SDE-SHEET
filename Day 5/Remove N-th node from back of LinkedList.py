class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next==None:
            return None
        temp=head
        while n:
            temp=temp.next
            n-=1
        current=head
        if temp==None:
            head=head.next
            return head
        while temp.next:
            current=current.next
            temp=temp.next
        current.next=current.next.next
        return head
