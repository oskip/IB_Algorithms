# Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
#
# Example :
#
# Input :
#
# A : [1 5 3]
# k : 2
# Output :
#
# 1
# as 3 - 1 = 2
#
# Return 0 / 1 for this problem.


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        vals = {}
        for a in A:
            if a-B in vals or a+B in vals:
                print a,a-B
                return 1
            if a not in vals: vals[a] = True
        return 0


x = 97
arr = [ 34, 63, 64, 38, 65, 83, 50, 44, 18, 34, 71, 80, 22, 28, 20, 96, 33, 70, 0, 25, 64, 96, 18, 2, 53, 100, 24, 47, 98, 69, 60, 55, 8, 38, 72, 94, 18, 68, 0, 53, 18, 30, 86, 55, 13, 93, 15, 43, 73, 68, 29 ]
res = Solution().diffPossible(arr,x)
print res