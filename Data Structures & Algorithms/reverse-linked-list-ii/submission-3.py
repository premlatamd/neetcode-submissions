# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        h=head
        if h is None:
            return h

        if left==right:
            return h

        
        i=1
        temp=h
        curr=None
        while i<left:

            curr=temp
            temp=temp.next
            i+=1

        j=i
        temp1=temp
        curr1=temp
        pre=None
        while j <= right:

            temp1=temp1.next
            curr1.next=pre
            print(curr1.val)
            pre=curr1
            curr1=temp1
            j+=1
            

        print(curr,temp.val)
        temp.next=temp1

        if curr:
            curr.next=pre
            return head
        else:
            curr=pre
            return curr
        head=h
        print(h.val)
        return head


        

        """if i==left:
                pre=curr
                curr=temp
            temp=temp.next
                curr.next=pre
            print(curr.val,head.val)

        head.next=temp
        h=curr

        return h"""

            


        