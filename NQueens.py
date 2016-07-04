# The n-queens puzzle is the problem of placing n queens on an nxn chessboard such that no two queens attack each other.
#
# http://i.imgur.com/yaxpgda.png
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
#
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]


class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        self.A = A
        self.res = []
        curr = [["_"]*A for _ in range(A)]
        self.getNextQueen(curr, 0, 0)
        return self.res

    def getNextQueen(self, curr, rowNum, numQueens):
        cpyCurr = []
        cpyNumQueens = numQueens
        for r in curr:
            cpyCurr += [[e for e in r]]
        for i in range(self.A):
            if curr[rowNum][i] == "_":
                curr[rowNum][i] = "Q"
                numQueens+=1
            else: continue
            for j in range(0,self.A):
                if curr[j][i] == "_": curr[j][i] = "."
            for k in range(self.A):
                if curr[rowNum][k] == "_": curr[rowNum][k] = "."
            r = rowNum
            c = i
            while r > 0 and c > 0:
                r -= 1
                c -= 1
                if curr[r][c] == "_": curr[r][c] = "."
                # elif curr[r][c] == "Q": return
            r = rowNum
            c = i
            while r < self.A-1 and c < self.A-1:
                r += 1
                c += 1
                if curr[r][c] == "_": curr[r][c] = "."
                # elif curr[r][c] == "Q": return
            r = rowNum
            c = i
            while r < self.A-1 and c > 0:
                r += 1
                c -= 1
                if curr[r][c] == "_": curr[r][c] = "."
                # elif curr[r][c] == "Q": return
            r = rowNum
            c = i
            while r > 0 and c < self.A-1:
                r -= 1
                c += 1
                if curr[r][c] == "_": curr[r][c] = "."
                # elif curr[r][c] == "Q": return
            if rowNum < self.A-1: self.getNextQueen(curr, rowNum+1, numQueens)
            elif numQueens == self.A: self.res.append(["".join(e) for e in curr])
            curr = []
            numQueens = cpyNumQueens
            for row in cpyCurr:
                curr += [[e for e in row]]

print Solution().solveNQueens(6)

# [....Q. ..Q... Q..... .....Q ...Q.. .Q.... ] [...Q.. Q..... ....Q. .Q.... .....Q ..Q... ] [..Q... .....Q .Q.... ....Q. Q..... ...Q.. ] [.Q.... ...Q.. .....Q Q..... ..Q... ....Q. ]
# [....Q. ..Q... Q..... .....Q ...Q.. .Q.... ] [...Q.. Q..... ....Q. .Q.... .....Q ..Q... ] [..Q... .....Q .Q.... ....Q. Q..... ...Q.. ] [.Q.... ...Q.. .....Q Q..... ..Q... ....Q. ]