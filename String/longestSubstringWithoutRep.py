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


solution = Solution()
result = solution.lengthOfLongestSubstring("pwwkew")
print(result)