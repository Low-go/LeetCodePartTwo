class Solution:
    def urlify(self, s: str, num: int) -> str:

        res = []
        for i in range(num):
            if s[i] == " ":
                res.append("%20")
            else:
                res.append(s[i])

        print(len("".join(res)))
        return "".join(res)

        




solution = Solution()
result = solution.urlify("Mr John Smith ", 13)
print (result)