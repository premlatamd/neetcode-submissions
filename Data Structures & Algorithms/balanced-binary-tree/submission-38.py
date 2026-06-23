# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            d=deque([root])
            deapth=0

            while d:
                size=len(d)
                for i in range(size):
                    node=d.popleft()
                    if node.left:
                        d.append(node.left)
                    if node.right:
                        d.append(node.right)
                    
                deapth+=1
            return deapth


        if root is None:
            return True
        
        d=deque([root])
        
     
        while d:
          
            size=len(d)
        
            for i in range(size):
                node=d.popleft()
                h1=height(node.left)
                h2=height(node.right)

                if abs(h1-h2)>1:
                    print(node.val)
                    return False
                if node.left:
                    d.append(node.left)
                    
                    
                if node.right:
                    d.append(node.right)
                    
                


        
        return True 
                    


        