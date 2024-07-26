from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set = []
        for i in nums:
            if i not in set:
                set.append(i)
            else:
                return True
        return False
    # this brute force has a time complexity exceded


    # 
    def containsDuplicate2(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
          
            hashset.add(i)
        return False

solution = Solution()
result = solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
print(result)

