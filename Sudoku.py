class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        self.res = []
        currSudoku = []
        for row in A: currSudoku.append(list(row))
        self.sudokuIter(currSudoku, 0, 0)
        for i in range(len(self.res)):
            for j in range(len(self.res)):
                A[i] = [''.join(self.res[i])]
        print A

    def sudokuIter(self, A, rowNum, colNum):
        while A[rowNum][colNum] != ".":
            rowNum, colNum = self.getNextAddr(rowNum, colNum, len(A))
            if rowNum >= len(A):
                self.res = A
                return

        potValues = [str(i) for i in range(1,10)]
        for v in A[rowNum]:
            if v in potValues: potValues.remove(v)
        for r in A:
            if r[colNum] in potValues: potValues.remove(r[colNum])

        for val in potValues:
            currSudoku = []
            for row in A: currSudoku.append(list(row))
            currSudoku[rowNum][colNum] = val
            nextRowNum, nextColNum = self.getNextAddr(rowNum, colNum, len(A))
            if self.isValidSudoku(currSudoku):
                if nextRowNum < len(currSudoku):
                    self.sudokuIter(currSudoku, nextRowNum, nextColNum)
                else:
                    self.res = currSudoku
                    return

    def getNextAddr(self, rowNum, colNum, size):
        colNum += 1
        colNum %= size
        if colNum == 0: rowNum += 1
        return rowNum, colNum

    def isValidSudoku(self, A):
        columns = [[0]*10 for _ in xrange(10)]
        rows = [[0]*10 for _ in xrange(10)]
        squares = [[0]*10 for _ in xrange(10)]
        for i, row in enumerate(A):
            for j, e in enumerate(row):
                if e == ".": continue
                e = int(e)
                if columns[j][e] == 1: return False
                else: columns[j][e] = 1
                if rows[i][e] == 1: return False
                else: rows[i][e] = 1

                sqAddress = j/3
                if 3 <= i < 6:
                    sqAddress += 3
                elif 6 <= i < 9:
                    sqAddress += 6
                if squares[sqAddress][e] == 1: return False
                else: squares[sqAddress][e] = 1
        return True


print Solution().solveSudoku([ "....7....", "6..195...", ".......6.", "8...6...3", "...8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79" ])