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

    # Hahahaha I actually brute forced this I'm low key kinda happy. It has a time complexity of On^3

    # lets see online how to do one without brute force solution
    def longestPalindrome2(self, s: str) -> str:
        res = ""
        resLen = 0 # longest length initially set to 0

        for i in range (len(s)):
            # check odd length 
            l, r = i, i # they should be initialized to center position

            while l >= 0 and r < len(s) and s[l] == s[r]: # while we know this is a palindrome
                if (r - l + 1) > resLen: # if this palindrome is bigger update resLen
                    res = s[l: r+1] # saving the string inside from l positon to r position
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l: r+1] # saving the string inside from l positon to r position
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res



solution = Solution()
result = solution.longestPalindrome2("cbbd")
print(result)