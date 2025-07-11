
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashSet = set()

        res = 0
        l = 0

        for i in range(len(s)):
            while s[i] in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(s[i])

            res = max(res, i -l + 1)

        return res




solution = Solution()
result = solution.lengthOfLongestSubstring("aab")
print(result)