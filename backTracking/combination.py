from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):

            if ((sum(subset) + i) == target):
                subset.append(i)
                res.append(subset.copy())
                subset= []
                return
            elif ((sum(subset)+ i) > target):
                subset = []
                return

        dfs(candidates[0])
        return res


solution = Solution()
result = solution.combinationSum([2,3,6,7],7)
print(result)