from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        l = 0

        for i in range(len(prices)):

            if i + 1 < len(prices) and prices[i +1] is not None:
                for j in range(i + 1, len(prices)):
                    store = prices[j] - prices[i]
                    if store > highest:
                        highest = store
        
        return highest


solution = Solution()
result = solution.maxProfit([7,6,4,3,1])
print(result)