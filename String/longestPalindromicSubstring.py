class Solution:

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        for i in range(len(s)):
            for j in range(i +1, len(s) + 1):
                subString = s[i:j]
                if self.isPalindrome(subString):
                    if len(subString) > len(res):
                        res = subString

        return res
    
# this was a brute force method

solution = Solution()
result = solution.longestPalindrome("babad")
print(result)

