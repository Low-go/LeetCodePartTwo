from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        pointer = 0

        for i in range(len(nums)):
            save = nums[pointer]
            if nums[pointer] > target:
                if pointer == 0:
                    pointer = len(nums) -1
                else:
                    pointer -= 1
            elif nums[pointer] == target:
                return pointer
            elif nums[pointer] < target:
                if pointer == len(nums) -1:
                    return -1
                pointer += 1
        
        return -1

solution = Solution()
result = solution.search([4,5,6,7,0,1,2], 0)
print(result)