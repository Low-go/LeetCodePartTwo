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

        twoCounter = 0 # lol im so dumb, this is just a loop with less abstraction, that makes this On2
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
    
    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        answer = []
        fix = 1

        for i in range(len(nums)):
            if i == 0:
                answer.append(fix)
            else:
                fix *= nums[i -1]
                answer.append(fix)

        fix = 1

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                pass
            else:
                fix *= nums[i + 1] 
                temp = fix * answer[i]
                answer[i] = temp

        return answer


    




    




solution = Solution()
result = solution.productExceptSelf3([1,2,3,4])
print(result)