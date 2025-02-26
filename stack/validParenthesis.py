class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) <= 1:
            return False
              
        stack = []

        # hashmap for comparison
        map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for i in s:
            if i in map:
                stack.append(i)
            else:
                if not stack or map[stack[-1]] != i:
                    return False
                stack.pop()
        
        # if stack is empty or not
        print(stack)
        return len(stack) == 0


solution = Solution()
result = solution.isValid("()")
print(result)