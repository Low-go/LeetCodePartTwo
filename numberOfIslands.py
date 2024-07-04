from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid: #nothing inside
            return 0
        

        m = len(grid) # rows
        n = len(grid[0]) # columns
        visit = set()
        islands = 0

        for i in range (m):
            for j in range(n):
                if grid [i][j] == "1":

                    element = grid[i][j]

                #print(f"Element at ({i}, {j}) : {element}") #okay so i can target each individual element
        return islands





solution = Solution()
solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])