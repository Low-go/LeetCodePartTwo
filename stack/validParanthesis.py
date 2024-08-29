from collections import deque
# this is 100 percent a stack problem

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        pairs = {")" : "(", "]": "[", "}": "{"}

        for element in s:
            if element in pairs: # looping through closing values(keys)
                if stack and stack[-1] == pairs[element]: # if stack not empty and the opening in stack is equal to the maped closing one(which would be open)
                    stack.pop()
                else:
                    return False
            else:
                stack.append(element)

        return True if not stack else False # only return true if stack empty



 
        

solution = Solution()
result = solution.isValid("(){}[]")
print (result)