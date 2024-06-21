from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid) # rows
        n = len(grid[0]) # columns

        for i in range (m):
            for j in range(n):

                element = grid[i][j]

                print(f"Element at ({i}, {j}) : {element}")





solution = Solution()
solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])