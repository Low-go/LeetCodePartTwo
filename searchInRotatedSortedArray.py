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
    


    # Proper binary searchh implementation
    def search2(self, nums: List[int], target: int) -> int:
        # lets try and do a binary search if i even remember it correctly

        small = 0
        large = len(nums) - 1 

        
        while small <= large:
            mid = (small + large) // 2

            if target == nums[mid]:
                return mid
            
            # Left Portion
            if nums[small] <= nums[mid]:
                if target > nums[mid] or target < nums[small]:
                    small = mid + 1
                else:
                    pass

            else:
                pass

        
        return -1

solution = Solution()
result = solution.search2([4,5,6,7,0,1,2], 0)
print(result)