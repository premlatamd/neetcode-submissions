class Solution:

    def getSuccessor(self, node):
        node = node.right

        while node.left:
            node = node.left

        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:

            # Case 1: No left child
            if root.left is None:
                return root.right

            # Case 2: No right child
            if root.right is None:
                return root.left

            # Case 3: Two children
            successor = self.getSuccessor(root)

            root.val = successor.val

            root.right = self.deleteNode(root.right, successor.val)

        return root