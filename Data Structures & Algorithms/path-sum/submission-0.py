# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum=0
        def fun(root,sum):
            if root==None:
                return False

            sum+=root.val

            if root.left==None and root.right==None:
                
                if sum==targetSum:
                    return True
                sum-=root.val
                return False
    
            return fun(root.left,sum) or fun(root.right,sum)
        return fun(root,sum)
        




        