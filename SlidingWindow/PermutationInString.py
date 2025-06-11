class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_map = {}

        # creates a hasmap with character occurences
        for i in s1:
            if i in s1_map:
                s1_map[i] += 1
            else:
                s1_map[i] = 1

        
        window_map = {}

        for i in range(len(s2)):
            
        
            if s2[i] in window_map:
                window_map[s2[i]] += 1
            else:
                window_map[s2[i]] = 1


            if i >= len(s1):
                old_one = s2[i - len(s1)]
                window_map[old_one] -= 1
                if window_map[old_one] == 0:
                    del window_map[old_one]
            
            if window_map == s1_map:
                return True
        
        return False
        


solution = Solution()
result = solution.checkInclusion("ab", "eidbaooo")
print(result)