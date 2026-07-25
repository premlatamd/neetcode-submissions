"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        clone={}
        clone[node]= Node(node.val)
        q=deque([node])
        while q:
            l=q.popleft()
            #copy=Node(l.val)
            for nei in l.neighbors:
                if nei not in clone:
                    clone[nei]= Node(nei.val)
                    q.append(nei)
                clone[l].neighbors.append(clone[nei])
        
            
        return clone[node]

        
        """for i in range(len(node)):
            a=[]
            temp=Node(node[i].val)
            for j in node[i].neighbors:
                a.append(j.val)
            temp.neighbors=a
            ans.append(temp)
        print(ans)
        return ans"""

        