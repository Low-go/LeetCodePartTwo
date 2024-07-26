from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = {}
        final = []

        if not strs:  #edge cases mentioned on leetcode
            final.append(strs)
            return final
        elif len(strs) == 1:
            final.append(strs)
            return final
        
        for i in range(len(strs)):  #loop through all the words
            sorted_string = ''.join(sorted(strs[i])) #sort that word and store it
            if sorted_string in hash_map:
                hash_map[sorted_string].append(strs[i]) #append it to existing key list
            else:
                hash_map[sorted_string] = [] # if it does not exist create one with key as the sorted and list woth appended items
                hash_map[sorted_string].append(strs[i])


        for value in hash_map.values():  #now loop through hashmap values
            final.append(value)
        return final


solution = Solution()
result = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(result)