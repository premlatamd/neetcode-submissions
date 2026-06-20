# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=head
        s=set()
        if  head==None:
            return False
        while temp.next!=None:
            if temp not in s:
                s.add(temp)
            else:
                return True
            temp=temp.next
        return False
