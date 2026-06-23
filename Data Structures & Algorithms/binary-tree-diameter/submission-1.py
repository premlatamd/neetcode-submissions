# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
                

        def height(root: Optional[TreeNode]) -> int:
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

        def diameter(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            h1=0
            h2=0
            if root.left:
                left_tree=root.left
                h1=height(left_tree)

            if root.right:
                right_tree=root.right
                h2=height(right_tree)
           
            return h1+h2

        d=deque([root])
        max_dia=0
        while d:
            size=len(d)
            for i in range(size):
                node=d.popleft()
                dia=diameter(node)
                if max_dia < dia:
                    max_dia=dia

                if node.left:
                    d.append(node.left)

                if node.right:
                    d.append(node.right)
        return max_dia

       
                        


            
        

        