from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        hold_array = []
        for i in intervals:
            for j in i:
                hold_array.append(j)

    

        return hold_array
        #return intervals


solution = Solution()
result = solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
print(result)