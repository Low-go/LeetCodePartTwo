from typing import List
import collections


# not done, I do not underdstand this completely yet so yea I will research breadth search before continuing this
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid: #nothing inside
            return 0
        

        m = len(grid) # rows
        n = len(grid[0]) # columns
        visit = set()
        islands = 0

        def bfs(i, j):
            q = collections.deque()
            visit.add((i, j)) # save as a tuple to kinda be like a single element
            q.append((i, j))

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions :
                    r, c = row + dr , col +dc

        for i in range (m):
            for j in range(n):
                if grid [i][j] == "1" and (i, j) not in visit: # so if the element is land
                    bfs(i, j) #breath first search
                    islands += 1

                    #element = grid[i][j]

                #print(f"Element at ({i}, {j}) : {element}") #okay so i can target each individual element
        return islands





solution = Solution()
solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])