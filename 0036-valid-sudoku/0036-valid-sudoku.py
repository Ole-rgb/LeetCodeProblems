columns = [[(r,c) for r in range(9)] for c in range(9)]
rows = [[(r,c) for c in range(9)] for r in range(9)]
blocks = [[(r,c) for r in range(br, br+3) for c in range(bc, bc+3)] for br in range(0,9,3) for bc in range(0,9,3)]

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.is_valid(rows, board) and self.is_valid(columns, board) and self.is_valid(blocks, board)
    
    def is_valid(self, constraints, board):
        for constraint in constraints:
            s = set()
            for (i,j) in constraint:
                if board[i][j] == ".":
                    continue
                if int(board[i][j]) in s:
                    return False
                s.add(int(board[i][j]))
        return True
