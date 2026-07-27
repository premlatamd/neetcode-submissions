# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level=0
        q=deque([(level,root)])
        d=defaultdict(list)
        while q:
            l,node=q.popleft()
            d[l].append(node.val)
            if node.left:
                q.append((l+1,node.left))
            if node.right:
                q.append((l+1,node.right))

        ans=[]
        for i in d.values():
            ans.append(i)
        return ans

            
            




            
            





        