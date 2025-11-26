from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new = set()
        for i in range(len(nums)):
            new.add(nums[i])

        new_array = list(new)
        new_array.sort()

        # tracks the current loo
        counter = 0
        # highest amount of consectuvie sequences
        highest = 0
        # tracks the number we would epxect to be on
        current = 0

        for i in range(len(new_array)):

            if (current + 1 == new_array[i]):
                current = new_array[i]
                counter += 1

                if counter >= highest:
                    highest = c

            current = new_array[i]
            

            if counter >= highest:
                highest = counter

            


        return new_array




solution = Solution()
result = solution.longestConsecutive([100,4,200,1,3,2])
print(result)