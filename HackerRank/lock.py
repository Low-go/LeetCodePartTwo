
class Solution():
    def lock(self, events):

        stack = []

        for i in range(len(events)):

            word = events[i].split()
            first_word = word[0]
            second_word = int(word[1])

            if first_word == "ACQUIRE":
                stack.append(second_word)
            
            elif first_word == "RELEASE":
                if second_word == stack[-1]:
                    stack.pop()
                else:
                    print(stack)
                    return i + 1
        
        print(stack)
        if len(stack) == 0:
            return 0
        


solution = Solution()
result = solution.lock(["ACQUIRE 234", "RELEASE 234", "ACQUIRE 111", "ACQUIRE 534", "RELEASE 534", "RELEASE 111"])
print(result)