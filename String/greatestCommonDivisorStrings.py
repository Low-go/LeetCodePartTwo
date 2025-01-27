class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # Okay this is not an easy question, that was a lie
        len1, len2 = len(str1), len(str2)

        # helper function
        def isDivisor(l):

            # first is l a factor(divisbale) into both strings
            if len1 % l or len2 % l: # if its none zero
                return False
            
            f1, f2 = len1 // l, len2 // l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2 # if the string multiplied that many times equals the other


        # we are looping backwards
        for l in range(min(len1, len2), 0, -1): # we are looping at the shortest strings value
            if isDivisor(l): # we create a helper function which takes a string from beggining to l


                # if the function returned true that means we found the result
                return str1[:l]
        
        return ""


solution = Solution()
result = solution.gcdOfStrings("AB", "ABABABAB")
print(result)
