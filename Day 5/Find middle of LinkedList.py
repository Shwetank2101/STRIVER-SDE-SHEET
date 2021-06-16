class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head.next==None:
            return head
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
