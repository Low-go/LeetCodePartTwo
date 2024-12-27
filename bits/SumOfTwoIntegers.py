class Solution:
    def getSum(self, a: int, b: int) -> int:
        pass

    # returns binary integer, or should i return a string?
    def bitMe(self, take):

        next = take # this should hold the next number to be worked on
        final = "" # originally a string

        while (next != 0):
            
            remainder = str(next % 2)
            final += remainder
            next = next // 2
    
            
          
        
        final = final[::-1]
        final = int(final)
        return final

# this is as far as I got with my own attempt, will switch to java as that is 
# what tutorials are recommending




solution = Solution()
result = solution.bitMe(1)
print(result)