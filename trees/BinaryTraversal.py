import collections
from typing import List

class Solution:
    # utilize a breadth first search algorithm, utilizing a queue
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = [] # final result

        # queue in python
        q = collections.deque()
        q.append(root) #lets throw that bad boy in there

        while q: # so long it aint empty or null
            
            qLen = len(q) # every loop we will do a second loop for this length
            level = []

            for i in range(qLen):
                node = q.popleft() # pop that bad boy

                if node: # check if not null
                    level.append(node.val) # add that bad boy
                    q.append(node.left)
                    q.append(node.right)
            
            # we out of the mini for loop lets add the level to final list if not empty
            if level:
                res.append(level)

        #return
        return res
                    

