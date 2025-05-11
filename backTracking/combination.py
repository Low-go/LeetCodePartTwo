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


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []


        def dfs(i, cur, total):
            # we acheived what we wanted
            if total == target:
                res.append(cur.copy())
                return
            # if our pointer exceeds length or total is larger than target
            if i >= len(candidates) or total > target:
                return

            # one tree where the candidate is included
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # in this one we did not include it
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res


solution = Solution()
result = solution.combinationSum([2,3,6,7],7)
print(result)