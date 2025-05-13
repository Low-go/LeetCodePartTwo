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
    
    def maxProfit2(self, prices: List[int]) -> int:

        '''
        The online solution is intersting. The way sliding window is implemented, 
        left and right pointers are initialzied but they are conditional
        the left one will incremet if the right one is smaller than it

        '''


        l, r  = 0, 1 # left is buying, right is selling
        maxProfit = 0

        while r < len(prices):

            # is this profitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                # whichever one is larger is assigned but
                # is this efficient
                maxProfit = max(maxProfit, profit)

            # in this case we are assuming that the next number is smaller than us
            # and we want the smallest number to be the buying number
            # so we move it all the way to that new right since its the smallest
            else:
                l = r
            r += 1


        return maxProfit




solution = Solution()
result = solution.maxProfit([7,6,4,3,1])
print(result)