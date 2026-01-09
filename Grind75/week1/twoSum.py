from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        # First thing we do is load a hashmap with this stuff
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        
        # next we loop again and check the hashmap
        for i in range(len(nums)):
            tempNumber = target - nums[i]
            if tempNumber in hashMap and hashMap[tempNumber] != i:
                return [i,hashMap[tempNumber]]
            
            return []


solution =Solution()
result = solution.twoSum([3, 2, 4], 6)
print(result)