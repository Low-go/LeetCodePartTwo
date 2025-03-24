

class Solution:


    def palindrome(self, s):
        return s == s[::-1]
    
    def subString(self, s):
        res = 0

        for i in range(len(s)):
            for j in range( i + 1, len(s) + 1):
                sub_string = s[i:j]
                if (self.palindrome(sub_string)):
                    res += 1
        print (res)
        return res


solution = Solution()
result = solution.subString("racecar")
print(result)
