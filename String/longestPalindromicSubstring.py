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
    
    def longestPalindrome2(self, s: str) -> str:

        res = ""
        resLen = 0

        # loop through each letter
        for i in range(len(s)):
            # odd length

            # initialize to pointers, where we are is the center
            l, r = i, i

            # this while loop is to move it outwards but make sure it
            # is within the bounds of the string, so t cant go below zero and cant be equal to the end
            # for some reason that last part
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen: # check its the longest we have seen so far
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even
            l, r = i, + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res

# this was an online solution, O(n)^2 complexity

solution = Solution()
result = solution.longestPalindrome("babad")
print(result)

