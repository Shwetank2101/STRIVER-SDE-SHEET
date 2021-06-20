class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head==None:
            return None
        temp1=temp2=head
        count=0
        prev=None
        while temp1:
            count+=1
            prev=temp1
            temp1=temp1.next
        k=k%count
        while k:
            k-=1
            temp2=temp2.next
        temp1=head
        if temp2==None:
            return
        while temp2.next:
            temp2=temp2.next
            temp1=temp1.next
        prev.next=head
        head=temp1.next
        temp1.next=None
        return head
        
