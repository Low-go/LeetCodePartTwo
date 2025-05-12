import operator
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        map = {
            "+": operator.add,
            "-": operator.sub,
            "/": operator.truediv,
            "*": operator.mul
        }

        for i in tokens:
            if i in map:
                var2 = stack.pop()
                var1 = stack.pop()
                mini_res = int(map[i](var1, var2))
                stack.append(mini_res)
            else:
                store = int(i)
                stack.append(store)
        res = stack.pop()
        return res



solution = Solution()
result = solution.evalRPN(["4","13","5","/","+"])
print(result)