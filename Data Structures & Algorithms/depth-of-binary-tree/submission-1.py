# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        s=deque()
        s.append((root,1))
    
        deapth=0
        while s:
            node,m=s.popleft()
            if node.left:
                s.append((node.left,m+1))
            if node.right:
                s.append((node.right,m+1))

        return m
        """while s:
            size=len(s)
            for i in range(size):
                node=s.popleft()


                if node.left:
                    s.append(node.left)
                    
                if node.right:
                    s.append(node.right)
                
            deapth+=1

        return deapth"""
            
               

            
        