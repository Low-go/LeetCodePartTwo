from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        check = 0
        newArray = []

        for i in intervals:
            for j in i:
                newArray.append(j)
        

        for i in newArray:
            if check ==2: # we only need to replace the two new ones
                break
            elif newArray[i] == newArray[0] or newArray[i] == newArray[len(newArray) - 1]: # i dont think we need to check first and last 
                pass
            elif newInterval[check] > newArray[i -1] and newInterval[check] > newArray[i]: # takes care of replacing
                newArray[i - 1] = newInterval[check]
                check += 1
            elif newInterval:
                pass

    
        # one last for loop to put the nums back into arrays/intervals
        # this was a horrible solution and I suck

    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # if the new interval is less than the first number
                res.append(newInterval)
                return res + intervals[i:] # we know everything after that will be ok
            # if the first number in new Intervals is 
            # greater that means we know there is no overlap before
            # meaning we can take everything before and append, it is safe
            elif newInterval[0] > intervals[i][1]: 
                res.append(intervals[i])
            else: # in this case there is overlap
                newInterval =  [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res




                

    


solution = Solution()
result = solution.insert2([[1,3], [6,9]], [2,5])
print(result)