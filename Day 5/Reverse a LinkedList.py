class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr is not None:
            head = curr.next
            curr.next = prev
            prev = curr
            curr = head
        return prev
