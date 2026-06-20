# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==[]:
            return head

        temp=head
        pre=None
        curr=head
        while temp!=None:
            temp=temp.next
            curr.next=pre
            
            pre=curr
            curr=temp
        head=pre
        return head

            

        