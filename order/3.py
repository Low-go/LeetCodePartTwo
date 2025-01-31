class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        

        l = 0
        res = 0 # final output


        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(s[r])

            res = max(res, r - l + 1)

        return res
        

solution = Solution()
result = solution.lengthOfLongestSubstring("pwwkew")
print(result)

     