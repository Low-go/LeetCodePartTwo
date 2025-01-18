from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        res = 0

        summation = sum(nums) # get max array

        l, r = 0, len(nums) - 1

        for i in range (len(nums)):
            
            storeLeft = nums[l]
            storeRight = nums[r]

            if summation - storeLeft > summation - storeRight:
                l += 1
                summation = summation - storeLeft
            else:
                r -= 1
                summation = summation - storeRight
            
            if summation > res:
                res = summation


        return res

        # my code was bad, did not even pass the basic test cases


    def maxSubArray2(self, nums: List[int]) -> int:
        # we begin by initializing the largest array number to 
        # the first value in the array

        maxSub = nums[0] 
        curSum = 0

        for n in nums:
            if curSum < 0: # if it gets negative we reset it back because nothing before really matters if it got this bad
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum) # get whichever one is higher and save it. 
        return maxSub

        # This is such a brilliant yet simple solution and it works at O(n) time. Wow
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
result = solution.maxSubArray([2,2,2])
print(result)