from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {} # keeps track
        for i in range(len(nums)):
            left_over = target - nums[i] # the value we are looking for
            if left_over in hashmap: # if it exists in hashmap
                return [hashmap[left_over], i] # then we want the indice of that leftover and the current indice whos number complimented it
            hashmap[nums[i]] = i #if not just append




solution = Solution()
result = solution.twoSum()
print(result)