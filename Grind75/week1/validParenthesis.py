class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []

        for i in s:
            if i in map: # if it is a key:
                stack.append(map[i])
            else:
                if not stack or stack.pop() != i: # not stack makes sure it is not empty, and yes you may do pops in conditional statments
                    return False

        
        return not stack

solution =Solution()
result = solution.isValid("()")
print(result)