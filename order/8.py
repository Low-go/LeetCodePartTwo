class Solution:
    def myAtoi(self, s: str) -> int:
        # to do this I might need to loop
        # need to check if its an alphabet chaarcter, or if its a 
        # number somehow

        res = ""
        digitChecked = False
        isNegative = False

        for i in s:

            # first step
            if (i == " "):
                continue
            
            if (digitChecked == False):
                if (i == "-"):
                    isNegative = True
                    continue

                if (i == "+"):
                    continue


            if (i.isdigit()):
                digitChecked = True
                res += i
            elif (i.isdigit() != True): # if digitchecked false hopefully
                break

        if (not res):
            res += "0"

        res = int(res)

        if (isNegative):
            res *= -1

        if (res > 2147483647):
            res = 2147483647
        elif(res < -2147483648):
            res = -2147483648            
        
        return res



        # I need to fix this dhit check, because like hmm
        # fir i check for - or +, because if i dont 





solution = Solution()
result = solution.myAtoi("+-12")
print(result)