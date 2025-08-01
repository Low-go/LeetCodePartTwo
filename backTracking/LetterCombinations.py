from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
                
        res =[]
        
        phoneTable = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }


        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in phoneTable[digits[i]]: # this is the values table of the current letter
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")


        return res




solution = Solution()
result = solution.letterCombinations("23")
print(result)
