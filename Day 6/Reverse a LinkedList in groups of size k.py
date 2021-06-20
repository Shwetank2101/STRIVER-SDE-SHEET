# Recursion
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr=head
        for i in range(k):
            if not curr:
                return head
            curr=curr.next
        prev=None
        current=head
        count=0
        for _ in range(k):
            next=current.next
            current.next=prev
            prev=current
            current=next
        head.next=self.reverseKGroup(next,k)
        return prev
            
