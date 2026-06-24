# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if root is None and subRoot is None:
                return True

            if root is None or subRoot is None:
                return False

            if root.val!=subRoot.val:
                return False

            d1=deque([root])
            d2=deque([subRoot])
            while d1:
                size=len(d1)
                for i in range(size):
                    
                    node2=d2.popleft()
                    node1=d1.popleft()
                    if node1.left and node2.left:
                        if node1.left.val != node2.left.val:
                            return False
                        d1.append(node1.left)
                        d2.append(node2.left)

                    if node1.right and node2.right:
                        if node1.right.val != node2.right.val:
                            return False
                        d1.append(node1.right)
                        d2.append(node2.right)
                    
                    if (node1.left and node2.left is None) or (node1.right and node2.right is None):
                        return False

                    if (node2.left and node1.left is None) or (node2.right and node1.right is None):
                        return False

            return True

        s=[root]
        while s:
            node1=s.pop()
            if sameTree(node1,subRoot):
                return True

            if node1.right:
                s.append(node1.right)

            if node1.left:
                s.append(node1.left)

        return False

       


        