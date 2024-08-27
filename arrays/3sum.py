from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        final = [] 

        # first lets try a primary loop it will iterate over every element
        for i in range(len(nums)):

            target += nums[i]

            hashmap = {} # this will be to imitate two sums original solution

            #now one more time, within the second loop we do the original twosums problem, 
            for j in range(len(nums)):
                
                if nums[j] == nums[i]: # ignore i's variable >:0
                    pass


solution = Solution()
result = solution.threeSum()
print (result)