class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        for i, e in enumerate(A):
            current = e
            if A[i] > i:
                A[i] = A[A[i]]
            elif A[i] < i:
                A[i] = A[A[i]] >> 16
            A[i] += e << 16
        for i in xrange(0, len(A)):
            A[i] &= 0xFFFF
        return A

print Solution().arrange([ 4, 0, 2, 1, 3 ])
