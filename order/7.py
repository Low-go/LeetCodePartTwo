class Solution:
    def reverse(self, x: int) -> int:
        # this is a weird question and I feel it is a trick
        
        store = ""
        negative = 1
        if ( x < 0):
            negative = -1
            store = str( x * -1)
        else:
            store = str(x)
                        
        
        secondStore = store[::-1]

        res = int(secondStore) * negative

        if (res > 2 ** 31 or res < -2 ** 31):
            return 0

        return res 


solution = Solution()
result = solution.reverse(-120)
print(result)