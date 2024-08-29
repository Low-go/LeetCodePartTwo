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

# youtube video assisted solution
class Solution:
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) -1

            while l < r :
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res



solution = Solution()
result = solution.threeSum2([-3,3,4,-3,1,2])
print (result)