from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # I wonder if I could use the same logic as the
        # product question

        maxProd = nums[0]
        curProd = 1 # I hope this isnt an issue with 0's

        for n in nums:

            if curProd < 0:
                curProd = 1
            curProd *= n
            maxProd = max(maxProd, curProd)
        return maxProd


solution = Solution()
result = solution.maxProduct([-2,0,-1])
print(result)