# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def presentNode(root:TreeNode,d:int) -> bool:
            if root is None:
                return False
            if root.val<d:
                return presentNode(root.right,d)
            elif root.val>d:
                return presentNode(root.left,d)
            elif root.val == d:
                return True
            else:
                return False
        print(root.val)
        if presentNode(root,p.val)  and  presentNode(root,q.val):
            if p.val <= root.val and q.val>=root.val:
                return root

            if q.val<=root.val and p.val>=root.val:
                return root

            if p.val <=root.val:
                node=root.left
                return self.lowestCommonAncestor(node,p,q)

            if q.val >=root.val:
                node=root.right
                return self.lowestCommonAncestor(node,p,q)

            


        return root
        
        