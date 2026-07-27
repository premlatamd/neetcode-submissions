# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque,defaultdict

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        l=0
        q=deque()
        q.append((l,root))
        d=defaultdict(list)
       
        while q:
            l,node=q.popleft()
            d[l].append(node.val)
            if node.right:
                q.append((l+1,node.right))
                
            if node.left:
                q.append((l+1,node.left))
        ans=[]
        for i in d.values():
            ans.append(i[0])
        print(ans)
        return ans


        
        