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

        def recursion(node):
            nonlocal res

        
            if not node:
                return 0
            
            height1 = recursion(node.left)
            height2 = recursion(node.right)
            

            current_diamter = height1 + height2
            res = max(res, current_diamter)


            return 1 + max(height1, height2)
        
        recursion(root)

        return res
        


    



        
        return res



root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
solution = Solution()
result = solution.diameterOfBinaryTree(root1)
print(result)