from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        columnMap = {j: set() for j in range(len(board[0]))} # hopefully this will take care of logic with the column

        squareMap = {(i//3, j//3): set() for i in range(9) for j in range(9)}
        
        for i in range(len(board)):

            rowSet = set() # this should take care of row logic

            for j in range(len(board[i])):

                if board[i][j] == '.':
                    continue

                if board[i][j] in rowSet:
                    return False
                rowSet.add(board[i][j])
                
                if (board[i][j] in columnMap[j]):
                    return False
                columnMap[j].add(board[i][j])

                square_key = (i//3, j//3)
                if board[i][j] in squareMap[square_key]:
                    return False
                squareMap[square_key].add(board[i][j])

        return True




solution = Solution()
result = solution.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".","3","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
print(result)