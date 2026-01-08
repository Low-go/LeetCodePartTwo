from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        #O(n)
        # min = 999999

        # for i in nums:
        #     if i < min:
        #         min = i
        # return min

        #O(logn)
        
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # logic to move left or right

            if nums[mid] > nums[right]:
                left = mid+ 1
            else:
                right = mid 


        
        return nums[left]

solution = Solution()
result = solution.findMin([3,4,5,6,1,2])
print(result)