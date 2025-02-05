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




solution = Solution()
result = solution.convert("paypalishiring", 3)
print(result)