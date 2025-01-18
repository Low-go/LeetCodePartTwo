from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if nums[0] == 0:
            return False
        
        current = 0

        while current != len(nums) - 1:
            pass


'''
proposed solution

* I dont know how to break from this

* Calculate all steps and find teh max between them and choose the one

with more steps available
'''



solution = Solution()
result = solution.canJump()
print(result)
