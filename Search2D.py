
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        start = 0
        m = len(A)-1
        stop = m
        while start <= stop:
            middle = (start+stop)/2
            if A[middle][0] == B:
                return 1
            elif (A[middle][0] < B and middle == m) or (A[middle][0] < B < A[middle+1][0]):
                return self.searchInRow(middle, A, B)
            elif A[middle][0] > B:
                stop = middle-1
            else:
                start = middle+1
        return 0

    def searchInRow(self, row, A, B):
        start = 0
        n = len(A[row])-1
        stop = n
        while start <= stop:
            middle = (start+stop)/2
            if A[row][middle] == B:
                return 1
            elif A[row][middle] > B:
                stop = middle - 1
            else:
                start = middle + 1
        return 0


print Solution().searchMatrix([[1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]], 321)
