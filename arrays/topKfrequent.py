from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        final = []
        for i in nums:
            if i in dict:
                dict[i] += 1 #increment the number 
            else:
                dict[i] = 1 # has not appeared

        for i in range(k):
            highest_key = max(dict, key=dict.get)
            final.append(highest_key)
            dict[highest_key] = 0
        
        return final


#got it easy as pieeee
        



solution = Solution()
result = solution.topKFrequent([1,2], 2)
print(result)