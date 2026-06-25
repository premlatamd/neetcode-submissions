# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp=head
        i=0
        while temp:
            temp=temp.next
            i+=1

        l=i
        if l%2!=0:
            mid=l//2+1
        else:
            mid=l//2

        temp=head
        
        j=0
        while j<mid:
            pre=temp
            temp=temp.next
            j+=1
        pre.next=None
        h1=temp


        temp=h1
        pre=None
        curr=h1
        while temp!=None:
            temp=temp.next
            curr.next=pre
            
            pre=curr
            curr=temp
        h1=pre
        



        first = head
        second = h1

        t1=head
        while t1:
            print(t1.val)
            t1=t1.next

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


        