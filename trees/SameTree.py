from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # they are exact
            return True
        if not p or not q or p.val != q.val:
            return False  # there exists a node on one side but not the other,or values not equal
       
       # ahhhh this is what was throwing me off finally
       # we paranthesis both cases, and and them so we can only return 
       # true if both cases are true, that makes so much sense

        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right) )

        