class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Solution:

    def reverseString(self, s: List[str]) -> None:
        if len(s)==1 or len(s)==0:
            return s
        a=[1]*len(s)
        for j,i in enumerate(s):
            a[j]=Node(i)
        
        for i in range(0,len(s)-1):
            a[i].next=a[i+1]
          
        head=Node(a[0].data)
        head.next=a[1]
        curr=head
        prev=None
        temp=head.next
        
        while temp!=None:
            prev=curr
            curr=temp
            temp=temp.next
            curr.next=prev
        head=curr
        

        curr=head
        i=0
        while curr!=None and i < len(s):
            s[i]=curr.data
            print(curr.data)
            curr=curr.next
           
            i+=1
        

        

    
        """a=[]
        p=""
        for i in s:
            p+=i
      
        for i in range(len(s)-1,-1,-1):
            a.append(p[i])

        print(p)"""
        """
        Do not return anything, modify s in-place instead.
        """
        