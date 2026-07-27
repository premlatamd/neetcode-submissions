# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def successor(self,node):
        node=node.right
        while node.left and node:
            node=node.left
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root==None:
            return root

        if key<root.val:
            root.left=self.deleteNode(root.left,key)

        elif key>root.val:
            root.right=self.deleteNode(root.right,key)
        else:
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right

            if root.left and root.right:
                succ=self.successor(root)
                root.val=succ.val
                root.right=self.deleteNode(root.right,succ.val)

        return root


        