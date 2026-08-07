# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n=0
        def dfs(node,n,k):
            
            if node==None:
                return 

            return dfs(node.left,n,k)
            # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n=0
        m=0
     
        def dfs(node,k):
            nonlocal n
            nonlocal m
            if node==None:
                return 

            dfs(node.left,k)
            n+=1
            print(node.val,k)
            if n==k:
                print(node.val,k)
                m=node.val
                return m
            dfs(node.right,k)
            return m
            
        return dfs(root,k) 
            
            
            

        