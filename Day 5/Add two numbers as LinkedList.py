class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first=l1
        second=l2
        carry=0
        while(first or second):
            a=first.val if first else 0
            b=second.val if second else 0
            sum1=a+b
            if carry:
                sum1+=1
            carry=0 if sum1<10 else 1
            sum1=sum1 if sum1<10 else sum1%10
            
            if first:
                first.val=sum1
                prev1=first
                first=first.next
            else:
                prev1=None
            if second:
                second.val=sum1
                prev2=second
                second=second.next
            else:
                prev2=None
        if carry:
            if prev1:
                prev1.next=ListNode(carry)
                return l1
            else:
                prev2.next=ListNode(carry)
                return l2
        else:
            if prev1:
                return l1
            else:
                return l2
