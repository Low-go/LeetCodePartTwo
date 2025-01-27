
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # these variables are used to track the index we need to get from the word next
        wordTraverse1 = 0
        wordTraverse2 = 0


        loopCount = len(word1) + len(word2)

        # we use a boolean to see if we are doing word 1 or word 2 next
        turn = True

        res = ""


        for i in range(loopCount):
            if turn: # we start with word 1 in this case
                res += word1[wordTraverse1]
                wordTraverse1 += 1

                # we only switch if the next word still has more letters
                if wordTraverse2 < len(word2):
                    turn = False
            else:
                res += word2[wordTraverse2]
                wordTraverse2 += 1

                if wordTraverse1 < len(word1):
                    turn = True
        
        return res


solution = Solution()
result = solution.mergeAlternately("ab", "pqrs")
print(result)
