import math

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        if A == 0 or B == 0: return 0
        if A == 1 or B == 1: return 1
        return math.factorial(A+B-2)/(math.factorial(A-1)*math.factorial(B-1))

print Solution().uniquePaths(12,30)