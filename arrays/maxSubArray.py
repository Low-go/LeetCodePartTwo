from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = sum( [-1, -2, 6, -2, -1])

        return res
    
'''
I LOWKEY think I have an algorithm that works without using the popular algorithm for this 
problem

* Start with a res = 0

* do a sum(arr) to get the max value of that array

* Loop through the length of the array 

* have a left and right pointer, one at beggining of array one at end

* each loop you check if the current number(which was initially calculated through sum(arr)) from each end of the array would make this number increase or decrease

* the number that would be least negative to remove or beenficial you remove and caluclate the new current, also if current is bigger than res replace rs for it

* do it n times until your done. Return res

* Only questions is which side for pointer to move up when both sides have the same number
'''

solution = Solution()
result = solution.maxSubArray(3)
print(result)