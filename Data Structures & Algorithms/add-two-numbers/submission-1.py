# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def convert(l1: Optional[ListNode]) -> int:
            if l1 is None:
                return 0
            i=0
            temp=l1
            sum=0
            while temp:
                sum+=temp.val*(10**i)
                temp=temp.next
                i+=1

            return sum

        
        n1=convert(l1)
        n2=convert(l2)

        n=n1+n2
        print(n1,n2,n)
        
        head=ListNode(n%10)
        curr=head
        temp=head
        n=n//10
        while n!=0:
            
            r=n%10
            n//=10
            temp=ListNode(r)
            if curr:
                curr.next=temp
            curr=temp

        return head
            
        