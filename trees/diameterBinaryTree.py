from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        if root.left or root.right is not None:
            res += 1

        def recursive():

            if root is None:
                return 0

            return 1 + self.diameterOfBinaryTree(root.left) + self.diameterOfBinaryTree(root.right)
        
        return res


root0 = TreeNode(0)
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
solution = Solution()
result = solution.diameterOfBinaryTree(root0)
print(result)