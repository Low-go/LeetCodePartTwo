from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # I wonder if I could use the same logic as the
        # product question

        maxProd = nums[0]
        curProd = 1 # I hope this isnt an issue with 0's

        for n in nums:

            if curProd == 0:
                curProd = 1
            curProd *= n
            maxProd = max(maxProd, curProd)
        return maxProd
    
    # this solution only passed half of the test cases

    def maxProduct2(self, nums: List[int]) -> int:
        res = max(nums) # just handy to start off with then 0. Also returns single arrays back
        curMin, curMax  = 1, 1

        for n in nums:
            if n == 0: # our 0 edge case so that we can set it to a neutral mult value
                curMin, curMax  = 1, 1
                continue 
            curMax = max(n * curMax, n * curMin, n) # this is confusing. I need to study more and come back tot his

        '''
        The best solution seems to be a crazy concept like what
        * It consists of finding the max and min of the first two elements. Store it
        
        * And from here on out each new element you multiply it by the previous max and min and store both of these new values

        *   
        '''

solution = Solution()
result = solution.maxProduct([-2,0,-1])
print(result)
