class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        for i in s:
            if i.isalnum():
                a += i.lower()

        return a == a[::-1]


solution = Solution()
result = solution.isPalindrome("A man, a plan, a canal: Panama")
print(result)