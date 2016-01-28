class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        i = 0
        j = len(A)-1
        add = True
        while 0 <= i < len(A) and 0 <= j < len(A):
            res = A[i]-A[j]
            if res > B:
                if add: j += 1
                if not add: i -= 1
            elif res < B:
                if add: i += 1
                if not add: j -= 1
            elif res == B and i != j: return 1
            if i == j and res == B: i -= 1

            add = not add
        return 0

print Solution().diffPossible([ 0, 1, 9, 10, 13, 17, 17, 17, 23, 25, 29, 30, 37, 38, 39, 39, 40, 41, 42, 60, 64, 70, 70, 70, 72, 75, 85, 85, 90, 91, 91, 93, 95 ], 83)