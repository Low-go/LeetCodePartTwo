from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []


        subset = []
        # function within a function to avoid passing variables
        # gonna try a backtracking depth first search
        # i is the index of the value we are making the decision on
        def dfs(i):

            # in this case we are out of bounds
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i] or the left tree
            # recursive search on the next element
            subset.append(nums[i])
            dfs(i + 1)

            #decision not to include nums[i], so we pop it, look at tree in notebook
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
            
            






        return res



solution = Solution()
result = solution.subsets([1,2,3])
print(result)