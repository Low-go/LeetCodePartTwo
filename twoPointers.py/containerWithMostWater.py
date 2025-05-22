from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        res = 0

        l, r = 0, 1

        while l <= len(height) - 1:


            if r >= len(height):
                l +=1
                r = l +1

                if r >= len(height):
                    break
                

            if height[l] < height[r]:
                hold = height[l]
            elif height[r] < height[l]:
                hold = height[r]
            else:
                hold = height[l]

            temp = hold * (r - l)

            if temp > res:
                res = temp
            
            r += 1

        
        return res




solution = Solution()
result = solution.maxArea([1,8,6,2,5,4,8,3,7])
print(result)