from typing import List

class Solution:
    def permutationsOfString(self, s: str, b: str) -> List[str]:
        res = []

        # hashmap to keep respective string and value
        map = {}


        # map now has numbers with respective times they appear
        for i in s:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1

        # how do I make a sliding window again?


        #window
        l, r = 0, len(s)

        while r <= len(b):

            temp_map = {}

            store = b[l:r]

            for i in store:
                if i in temp_map:
                    temp_map[i] += 1
                else:
                    temp_map[i] = 1


            if temp_map == map:
                res.append(store)

            l += 1
            r += 1

        return res
    

solution = Solution()
result = solution.permutationsOfString("abbc", "cbabadcbbabbcbabaabccbabc")
print (result)