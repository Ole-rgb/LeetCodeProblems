colums = [[(i,j) for i in range (0,9)] for j in range(0,9)] #(0,0), (0,1), ..., (0,8), (1,0), (1,1),..., (8,7), (8,8)
rows = [[(j,i) for i in range (0,9)] for j in range(0,9)]
blocks = [
    [((i // 3) * 3 + j // 3, (i % 3) * 3 + j % 3) for j in range(9)] for i in range(9)
]

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.valid(rows, board) and self.valid(colums, board) and self.valid(blocks, board)

    def valid(self,constraints: List[Tuple[int]],board: List[List[str]])->bool:
        for constraint in constraints:
            s = dict()
            for (x,y) in constraint:
                if board[x][y] ==  ".":
                    continue
                elif s.get(board[x][y]) is not None:
                    return False
                s[board[x][y]] = True
        return True