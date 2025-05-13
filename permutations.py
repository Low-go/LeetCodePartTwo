from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 1:
            return [nums.copy()]
        
        res = []
        res.append(nums.copy())
        amount = len(nums)

        # finds factorial

        for i in range(len(nums), 1, -1):
            amount *= (i - 1)

        p = 0
        for i in range(amount):
            
            if p >= len(nums) -1:
                p = 0

            nums[p], nums[p + 1] = nums[p+1], nums[p]
            p +=1
            res.append(nums.copy())

        return res
    

    def permute2(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res
        



        



solution = Solution()
result = solution.permute([1,2,3])
print(result)