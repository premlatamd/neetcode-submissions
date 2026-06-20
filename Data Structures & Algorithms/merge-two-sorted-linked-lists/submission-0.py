# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=list1
        temp2=list2
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        if temp1.val <= temp2.val:
            head=temp1
            temp1=temp1.next
        else:
            head=temp2
            temp2=temp2.next
        temp=head
        while temp1!=None and temp2!=None: 
            if temp1.val <= temp2.val:
                temp.next=temp1
                temp1=temp1.next
            else:
                temp.next=temp2
                temp2=temp2.next
            curr=temp
            temp=temp.next
        if temp1:
            temp.next=temp1
        if temp2:
            temp.next=temp2
        
        return head


            
        


