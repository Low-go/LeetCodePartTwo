from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        map = {j: set() for j in range(len(board[0]))} # hopefully this will take care of logic with the column
        
        for i in range(len(board)):

            rowSet = set() # this should take care of row logic

            for j in range(len(board[i])):

                if board[i][j] in rowSet:
                    return False
                
                if (board[i][j] in map[j]):
                    return False
                
                elif (board[i][j] != '.'):
                    rowSet.add(board[i][j])
                    map[j].add(board[i][j])

                


                
                



        return True




solution = Solution()
result = solution.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
print(result)