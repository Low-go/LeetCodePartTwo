from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total = 1
        final = []
        for i in range(len(nums)):
            total *= nums[i]
        
        
        for i in nums:
            if i == 0:
                final.append(0)
            else:
                num = total
                num //= i
                final.append(num)
        return final
    
    # this first solution was not allowed because it has a division operation
    
    def productExceptSelf2(self, nums: List[int]) -> List[int]:

        counter = 0
        final = []

        twoCounter = 0
        currentnumber = 1

        while counter < len(nums):

            if twoCounter == counter:
                twoCounter += 1
            
            else:
                currentnumber *= nums[twoCounter]
                twoCounter += 1

            if twoCounter >= len(nums):
                twoCounter = 0
                counter += 1
                final.append(currentnumber)
                currentnumber = 1
        
        return final
    

    # apparently time limit exceeded


    




solution = Solution()
result = solution.productExceptSelf2([-1,1,0,-3,3])
print(result)