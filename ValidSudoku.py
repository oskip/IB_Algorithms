# Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
# http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png
#
# The input corresponding to the above configuration :
#
# ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
# A partially filled sudoku which is valid.
#
#  Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        columns = [[0]*10 for _ in xrange(10)]
        rows = [[0]*10 for _ in xrange(10)]
        squares = [[0]*10 for _ in xrange(10)]
        for i, row in enumerate(A):
            for j, e in enumerate(row):
                if e == ".": continue
                e = int(e)
                if columns[j][e] == 1:
                    print i,j,"c"
                    return 0
                else: columns[j][e] = 1
                if rows[i][e] == 1:
                    print i,j,"r"
                    return 0
                else: rows[i][e] = 1

                sqAddress = j/3
                if 3 <= i < 6:
                    sqAddress += 3
                elif 6 <= i < 9:
                    sqAddress += 6
                if squares[sqAddress][e] == 1:
                    print i,j,"s"
                    return 0
                else: squares[sqAddress][e] = 1
        return 1


print Solution().isValidSudoku([ "..5.....6", "....14...", ".........", ".....92..", "5....2...", ".......3.", "...54....", "3.....42.", "...27.6.." ])