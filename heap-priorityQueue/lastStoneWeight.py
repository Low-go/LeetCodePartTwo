from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # python only does min heaps so to simulate a max heap
        # we will multiply the array by negatives so that its flipped

        stones = [-s for s in stones] # list comprehension, compact way to write a loop that builds a list
        # create a new list where each element is -s for each s taken from stone
        # [<expression> for <variable> in <iterable>]

        heapq.heapify(stones) # linear time operation

        while len(stones) > 1:
            first = heapq.heappop(stones) # returns the smalles element from the heap
            second = heapq.heappop(stones)

            if second > first: # this reverse is because all the weights are negative
                heapq.heappush(stones, first - second)

            stones.append[0] # edge case in case this is empty
            return abs(stones[0])

        pass


solution = Solution()
result = solution.lastStoneWeight()
print(result)