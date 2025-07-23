class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2

        if n== 3:
            return 3

        base1 = 2
        base2 = 3

        for i in range (0, n - 3):
            store = base2
            base2 = base2 + base1
            base1 = store
        return base2
solution = Solution()
result = solution.climbStairs(6)
print(result)