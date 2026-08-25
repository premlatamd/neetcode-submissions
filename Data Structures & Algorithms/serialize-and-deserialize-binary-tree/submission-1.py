# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q=deque()
        q.append(root)
        arr=[]
        while q:
            
            node=q.popleft()
            if node==None:
                arr.append("N")
                continue
            arr.append(node.val)
            
            q.append(node.left)
            q.append(node.right)

        while arr and arr[-1]=="N":
            arr.pop()
        
        temp = [str(i) for i in arr]

        s=",".join(temp)
        print(s)
        return s


        
    # Decodes your encoded data to tree.
    def deserialize(self, data):
        if not data:
            return None

        values = data.split(",")

        root = TreeNode(int(values[0]))
        q = deque([root])

        i = 1

        while q and i < len(values):
            node = q.popleft()

            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i += 1

            if i < len(values) and values[i] != "N":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            i += 1

        return root