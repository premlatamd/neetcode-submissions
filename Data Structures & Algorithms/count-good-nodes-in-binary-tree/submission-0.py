# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q=deque()
        q.append((root,root.val))
        count=0
        
        while q:
            node,maxi=q.popleft()
            
            if node.val >=maxi:
                count+=1
                
            maxi=max(maxi,node.val)

            if node.right:
                q.append((node.right,maxi))
            if node.left:
                q.append((node.left,maxi))

        return count

            
            

