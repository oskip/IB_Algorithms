class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        if len(A) < 2: return A
        n = len(A) - 1
        i = 0
        while i <= n / 2:
            for j in range(i, n - i):
                A[j][n - i], A[n - i][n - j], A[n - j][i], A[i][j] = A[i][j], A[j][n - i], A[n - i][n - j], A[n - j][i]
            i += 1
        return A


print Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
