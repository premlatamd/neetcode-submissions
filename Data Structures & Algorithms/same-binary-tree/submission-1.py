# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        d1=deque([p])
        d2=deque([q])

        while d1 and d2:
            node1=d1.popleft()
            node2=d2.popleft()

            if node1.val!=node2.val:
                return False
            

            if node1.left and node2.left:
                d1.append(node1.left)
                d2.append(node2.left)
                if node1.left.val!=node2.left.val:
                    return False
            
            if node1.right and node2.right:
                d1.append(node1.right)
                d2.append(node2.right)
                if node1.right.val!=node2.right.val:
                    return False

            if (node1.left and node2.left is None) or (node1.right and node2.right is None):
                return False

            if (node2.left and node1.left is None) or (node2.right and node1.right is None):
                return False



        
        
        return True


            

        