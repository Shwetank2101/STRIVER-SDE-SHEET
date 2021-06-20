class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        temp1=headA
        temp2=headB
        count1,count2=0,0
        while temp1:
            temp1=temp1.next
            count1+=1
        while temp2:
            temp2=temp2.next
            count2+=1
        diff=abs(count1-count2)
        if count1>count2:
            temp1=headA
            temp2=headB
        else:
            temp1=headB
            temp2=headA
        while diff:
            temp1=temp1.next
            diff-=1
        while temp1 and temp2 and temp1!=temp2:
            temp1=temp1.next
            temp2=temp2.next
        return temp1

#Circular linked list
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        linkA, linkB = headA, headB
        
        while ( linkA != linkB):
            
            linkA = headB if not linkA else linkA.next
            linkB = headA if not linkB else linkB.next
        return linkA
