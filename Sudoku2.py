class Solution:
    # @param A : list of list of chars
    # @return nothing
    def __init__(self):
        self.solution = []

    def solveSudoku(self, sudoku):
        self.solveSudokuHelper(sudoku)
        for i in range(9):
            sudoku[i] = self.solution[i]

    def solveSudokuHelper(self, sudoku, r=0, c=0):
        while sudoku[r][c] != '.':
            r, c = self.getNexPos(r,c)
            if r >= 9:
                self.solution = sudoku
                return

        vals = self.getPossibleValsForPos(sudoku, r, c)
        if len(vals) == 0: return
        for v in vals:
            sudokuCpy = [list(row) for row in sudoku]
            sudokuCpy[r][c] = v
            sudokuCpy = [''.join(row) for row in sudokuCpy]
            self.solveSudokuHelper(sudokuCpy, r, c)

    def getNexPos(self,r,c):
        nC = c+1
        nR = r
        if nC == 9:
            nR += 1
            nC = 0
        return nR,nC

    def getPossibleValsForPos(self, sudoku, r, c):
        if sudoku[r][c] != '.': return []
        vals = set([str(i+1) for i in range(9)])
        for row in range(9):
            if sudoku[row][c] in vals:
                vals.remove(sudoku[row][c])
        for col in range(9):
            if sudoku[r][col] in vals:
                vals.remove(sudoku[r][col])
        for pos in range(9):
            curr = sudoku[3*(r/3)+pos/3][3*(c/3)+pos%3]
            if curr in vals:
                vals.remove(curr)
        return [e for e in vals]

sudoku = [ "53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79" ]

Solution().solveSudoku(sudoku)
print sudoku