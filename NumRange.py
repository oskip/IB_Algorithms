# Given an array of non negative integers A, and a range (B, C),
# find the number of continuous subsequences in the array which have sum S in the range [B, C] or B <= S <= C
#
# Continuous subsequence is defined as all the numbers A[i], A[i + 1], .... A[j]
# where 0 <= i <= j < size(A)
#
# Example :
#
# A : [10, 5, 1, 0, 2]
# (B, C) : (6, 8)
# ans = 3
# as [5, 1], [5, 1, 0], [5, 1, 0, 2] are the only 3 continuous subsequence with their sum in the range [6, 8]
#
#  NOTE : The answer is guranteed to fit in a 32 bit signed integer.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        if len(A) < 1: return 0
        i = 0
        j = 0
        result = 0
        curSum = A[j]
        while i < len(A) and j < len(A):
            if C >= curSum >= B:
                result += 1
                if j >= len(A)-1: return result
                j += 1
                curSum += A[j]
            elif curSum < B:
                if j >= len(A)-1: return result
                j += 1
                curSum += A[j]
            else:
                curSum -= A[i]
                i += 1
        return result

print Solution().numRange([ 1, 4, 8, 5, 2, 3, 8, 7, 6, 10], 11, 13)