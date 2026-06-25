# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        temp=head
        while temp:
            temp=temp.next
            l+=1
        

        curr=head
        temp=head
        i=0
        while i<=(l-n):
            if (l-n)==0:
                temp=temp.next
                curr.next=None
                head=temp
                return head
            pre=curr
            curr=temp
            temp=temp.next
            i+=1

        if temp:
            pre.next=temp

        elif pre == curr:
            return None

        elif curr.next is None:
            pre.next=None

        return head

