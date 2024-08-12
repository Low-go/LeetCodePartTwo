from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:

        if (s == ""):
            return True
        
        lowercase = s.lower()
        final = ""



        for i in lowercase:
            if (i.isalnum()):
                final += i # final should now be a single string no alphanums

        
        flipped = final[::-1]

        print(final)
        print(flipped)
        
        
        if final == flipped:
            return True
        else:
            return False
                

solution = Solution()
result = solution.isPalindrome("A man, a plan, a canal: Panama")
print(result)