class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return 
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        if slow!=fast:
            return 
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow
