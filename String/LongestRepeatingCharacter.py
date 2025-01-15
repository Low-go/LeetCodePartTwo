class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # this will be another sliding window problem
        res = 0
        map = {}

        l = 0 # initial pointer 

        for r in range(len(s)):

            if s[r] in map:
                map[s[r]] += 1
            else:
                map[s[r]] = 1
                
            # calculate window size
            window = r - l +1

            # most frequent character 
            maxFrequency = max(map.values()) if map else 0

            if window - maxFrequency > k: # pointer moves if thats the case
                map[s[l]] -= 1 # decrease the occurance of that character
                l += 1 
            else:
                res = max(res, window)
        return res
'''
This whole algorithm works by 

* Creating a hashmap

* starting a left pointer at 0

* Looping through each letter

* add each letter to the map, if its not there add it and set its value to 1
  if it is, increment its number

* Calculate current window size

* In each loop check which character has the highest number value

* if the window minus the number of occurences of highest number is smaller or equal to replacment your good, just set
  res to the larger value of window or current res

* else, increment the pointer and since the legft character is lost to our windwo we access it s[l] in our map, and lower its frequency


'''



solution = Solution()
result = solution.characterReplacement("AABABBA", 1)
print(result)