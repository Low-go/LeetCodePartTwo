from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        # map to store key value

        # enumerate to have the object and iteration at once
        for i, num in enumerate(nums): 
            
            # this should be the opposite stored
            compliment = target - num

            # if its completing pair exists we found a match
            if compliment in map:
                return [map[compliment], i]
            else:
                map[num] = i
        return []    
    




solution = Solution()
result = solution.twoSum([2,7,11,15], 9)
print(result)
