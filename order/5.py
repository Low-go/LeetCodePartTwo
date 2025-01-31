class Solution:
    def longestPalindrome(self, s: str) -> str:
        # mofo lets brute force this dammit

        res = ""
        for i in range(len(s)): # loop s amount of times

            store = "" # temp string storage

            for j in range(i, len(s)): # we will check every possible mini possibility inside
                store += s[j]

                flip = store[::-1]

                if store == flip and len(store) > len(res):
                    res = store
        return res

# Hahahaha I actually brute forced this I'm low key kinda happy


solution = Solution()
result = solution.longestPalindrome("cbbd")
print(result)