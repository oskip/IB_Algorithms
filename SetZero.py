class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        n = len(A)
        m = len(A[0])
        storageColumn = -1
        storageRow = -1
        for i in range(0, n):
            for j in range(0, m):
                if A[i][j] == 0 and storageColumn == storageRow == -1:
                    storageRow = i
                    storageColumn = j
                    A[storageRow][storageColumn] = 2
                    for j2 in range(j, m):
                        if A[i][j2] == 0: A[storageRow][j2] = 2
                    for i2 in range(i, n):
                        if A[i2][j] == 0: A[i2][storageColumn] = 2
                elif A[i][j] == 0 and i != storageRow and j != storageColumn:
                    A[storageRow][j] = 2
                    A[i][storageColumn] = 2

        for i in range(0, n):
            if A[i][storageColumn] == 2 and i != storageRow:
                for j in range(0, m):
                    A[i][j] = 0
        for j in range (0, m):
            if A[storageRow][j] == 2 and j != storageColumn:
                for i in range(0, n):
                    A[i][j] = 0
        if storageColumn > -1 and storageRow > -1:
            for i in range (0, n):
                A[i][storageColumn] = 0
            A[storageRow] = [0] * m
        return A

print Solution().setZeroes([[1, 1],[1, 1]])