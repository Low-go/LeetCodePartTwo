from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # only add open paranthesis if open < n
        # only add a closing paranthesis if closed < open
        # valild IFF open == close == n
        
        if n == 1:
            return "()"

        # this has to be a backtracking solution

        res = []
        arr = []

        

        def dfs(open, close):

            if open == close == n:
                # join everything in our temp array and add to res
                return res.append("".join(arr))
            
            if open < n:
                arr.append("(")
                dfs(open +1, close)
                arr.pop()
            
            if close < open:
                arr.append(")")
                dfs(open, close + 1)
                arr.pop()
        
        dfs(0, 0)
        return res




solution = Solution()
result = solution.generateParenthesis()
print(result)