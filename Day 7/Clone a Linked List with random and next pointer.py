#O(n) Space
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        d={}
        d[None]=None
        temp=head
        while temp:
            d[temp]=Node(temp.val)
            temp=temp.next
        temp=head
        while temp:
            d[temp].next=d[temp.next]
            d[temp].random=d[temp.random]
            temp=temp.next
        return d[head]

#O(1) Space
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        temp=head
        while temp:
            next=temp.next
            temp.next=Node(temp.val)
            temp.next.next=next
            temp=temp.next.next
        temp=head
        while temp:
            if temp.random:
                temp.next.random=temp.random.next
            temp=temp.next.next
        dummy=Node(1)
        out=dummy
        temp=head
        while temp:
            out.next=temp.next
            temp.next=temp.next.next
            temp=temp.next
            out=out.next
        return dummy.next
