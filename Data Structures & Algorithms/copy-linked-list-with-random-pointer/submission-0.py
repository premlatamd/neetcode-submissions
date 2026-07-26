"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        orig=head
        if orig==None:
            return None
    
        clone={}
        clone[orig]=Node(orig.val)
        while orig!=None:
            if orig not in clone:
                clone[orig]=Node(orig.val)
            if orig.next!=None:
                if orig.next not in clone:
                    clone[orig.next]=Node(orig.next.val)
                clone[orig].next=clone[orig.next]
            if orig.random!=None:
                if orig.random not in clone:
                    clone[orig.random]=Node(orig.random.val)
                clone[orig].random=clone[orig.random]
            orig=orig.next


        return clone[head]
            
           


        