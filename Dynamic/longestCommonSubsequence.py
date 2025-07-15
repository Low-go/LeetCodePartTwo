class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m, n = len(text1), len(text2)

        # A more readable version of a dp list for me
        dp = []
        # i don't completely understand it but in dp we 
        # build up the solution from nothing, so we add a 1 on both
        # sides to represent that they start empty

        # our base case basically an empty string
        for _ in range(m+1): 
            dp.append([0] * (n+1))

        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j -1]:
                    dp[i][j] = dp[i -1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # wehn writing the graph it checks the top of it or to teh left, the higher nnumber is took
        
        return dp[m][n]



solution = Solution()
result = solution.longestCommonSubsequence("aggtab", "gxtxayb")
print(result)