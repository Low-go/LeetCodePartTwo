class Solution:
    def convert(self, s: str, numRows: int) -> str:


        if numRows == 1:
            return s
        
        # wave calculations 2 * (n -1)
        calc = 2 * (numRows - 1) # first and last loop calc

        res = ""

        # I think using arrays might be more efficient but Ill
        # switch up the strings when I am done with the major portion of the logic


        for i in range(numRows):
            j = i

            l = calc - 2 * i
            r = 2 * i
            leftTurn = True if i != 0 and i != numRows -1 else False # ahhhhhhhhhhhh my headdd

            while j < len(s):
                    
                # first and last rows
                if i == 0 or i == numRows -1:

                    res += s[j]
                    j += calc # add our counter to it

                else:
                    res += s[j]
                    if leftTurn:
                        j += l
                        leftTurn = False
                    else:
                        j += r
                        leftTurn = True
        return res


    # online solution does not look to diff from mine
    def convert2(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        res = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range (r, len(s), increment ): # i like his use of r here, we start from the next index 
                res += s[i]

                if (r > 0 and r < numRows -1 and i + increment - 2 * 
                    r < len(s)): # this is how he is checking for middle rows
                    
                    res += s[i + increment - 2 * r]

        return res

# ok so his code is probably faster more concise and better than mine
# but damn if it isn't less readable

solution = Solution()
result = solution.convert("paypalishiring", 3)
print(result)