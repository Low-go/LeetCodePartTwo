from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        
        secondListLength = len(nums) + 1
        noDuplicates = set()

        for i in range(secondListLength):
            noDuplicates.add(i)

        for i in nums:
            if i in noDuplicates:
                noDuplicates.remove(i)
        
        return noDuplicates.pop()

solution = Solution()
result = solution.missingNumber([3,0,1])
print(result)