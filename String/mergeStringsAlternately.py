
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


    #alternatively
    def mergeAlternately2(self, word1: str, word2: str) -> str:
        res = []

        min_length = min(len(word1), len(word2)) # grab the shortest length to loop

        for i in range(min_length): # append both till min_length
            res.append(word1[i])
            res.append(word2[i])

        res.extend(word1[min_length:]) # min_length: says starting from min length slice or add all the rest of the letters
        res.extend(word2[min_length:]) # this is also due to extend which addds all items from an iterable

        return ''.join(res) # we used an array over a strong because strings take up memnory and are immutable
        



solution = Solution()
result = solution.mergeAlternately2("ab", "pqrs")
print(result)
