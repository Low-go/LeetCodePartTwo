class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # this will be our final output
        res = 0
        holder = []

        for i in s: # lets loop through all of them :0

            if i in holder:
                temp = len(holder)

                # if the length is bigger lets replace it
                if temp > res:
                    res = temp

                # now discard previous array and add the one you have
                holder = []
                holder.append(i)
            else:
                holder.append(i)
        
        if len(holder) > res:
            res = len(holder)

        # return 
        return res

    # we are learning the sliding window today
    def lengthOfLongestSubstring2(self, s: str) -> int:
        charSet = set() # apparently they only allow unique values

        # for a sliding window we need two pointers,
        # the right pointer can literally be the for loop 
        # as it moves its way right, easier to manage
        l = 0 
        res = 0 # final output

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l]) # remove the leftmost character
                l += 1
            charSet.add(s[r])

            res = max(res, r - l + 1)
        return res

# my solution is not perfectly working as I would wish or hope 
solution = Solution()
result = solution.lengthOfLongestSubstring("pwwkew")
print(result)