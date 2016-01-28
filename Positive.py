

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        i = 0

        while i < len(A):
            pos = A[i]-1
            if 0 < A[i] <= n and (A[i] != A[pos]):
                A[i], A[pos] = A[pos], A[i]
                i -= 1
            i += 1

        for i in xrange(0, len(A)):
            if A[i] != i + 1:
                return i + 1
        return n + 1


print (Solution().firstMissingPositive(
    [-5,1,2]))