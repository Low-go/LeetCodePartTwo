class Solution:
    def climbStairs(self, n: int) -> int:
        x = 2
        y = 3

        if n == 1:
            print (1)
            return 1
        elif n < 3:
            print (x)
            return x
        else:
            for i in range(n-3):
                z = x+y
                x = y
                y = z

            print (y)
            return y



solution = Solution()
solution.climbStairs(4)