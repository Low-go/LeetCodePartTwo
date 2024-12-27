class Solution:
    def climbStairs(self, n: int) -> int:
        
        x = 2
        y = 3
        z = 0

        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        if n == 3:
            return 3
        
        store = n - 3

        for i in range(store):
            
            z = x + y
            x = y
            y = z
        
        return z


solution = Solution()
result = solution.climbStairs(5)
print(result)