from typing import List

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        

        def GCD(a, b):
            
            if b == 0:
                return a
            
            GCD(b, a%b)
        
        # my guess is this is a pointer problem


        res = 0

        for i in range(len(nums)):
            
            gcd_curr = 0

            for j in range( i, len(nums)):
                gcd_curr = GCD(gcd_curr, nums[j])

                if gcd_curr == k:
                    res += 1
                elif gcd_curr < k:
                    break
        return res

            
            
            
            


solution = Solution()
result = solution.subarrayGCD()
print(result)