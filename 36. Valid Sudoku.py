def isValidSudoku(self, board: List[List[str]]) -> bool:
    def chek_row(board):
        for i in range(9):
            c = [0]*9
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if c[int(board[i][j])-1] > 0:
                    return False
                c[int(board[i][j])-1]+=1
        return True

    def chek_col(board):
        for j in range(9):
            c = [0]*9
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if c[int(board[i][j])-1] > 0:
                    return False
                c[int(board[i][j])-1]+=1
        return True

    def chek_squer(board):
        for p,k in [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]:
            c = [0]*9 
            for i in range(3):
                for j in range(3):
                    if board[i+p][j+k] == '.':
                        continue
                    if c[int(board[i+p][j+k])-1] > 0:
                        return False
                    c[int(board[i+p][j+k])-1]+=1
        return True

    return chek_row(board) and chek_col(board) and chek_squer(board)
