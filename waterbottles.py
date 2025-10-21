class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles # start by drinking all of them
        emptyBottles = numBottles # we start with all of them empty
        
        while (emptyBottles >= numExchange):
            newBottles = emptyBottles // numExchange
            leftover = emptyBottles % numExchange
            
            drank += newBottles

            emptyBottles = newBottles + leftover
        return drank



solution = Solution()
result = solution.numWaterBottles(15, 4)
print(result)