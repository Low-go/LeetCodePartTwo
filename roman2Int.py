class Solution:
    def romanToInt(self, s: str) -> int:
        
        #hashmap for reference
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        
        res = 0
        skip = False

        for i in range(len(s)):

            if skip:
                skip = False
                continue

            if i < len(s) - 1:
                if (s[i] == "I" and s[i+1] == "V") or (s[i] == "I" and s[i+1] == "X"):
                    res += (map[s[i + 1]] - map[s[i]])
                    skip = True
                elif (s[i] == "X" and s[i+1] == "L") or (s[i] == "X" and s[i+1] == "C"):
                    res += (map[s[i + 1]] - map[s[i]])
                    skip = True
                elif (s[i] == "C" and s[i+1] == "D") or (s[i] == "C" and s[i+1] == "M"):
                    res += (map[s[i + 1]] - map[s[i]])
                    skip = True
                else:
                    res += map[s[i]]
            else:
                res += map[s[i]]

        return res



solution = Solution()
result = solution.romanToInt("IV")
print(result)