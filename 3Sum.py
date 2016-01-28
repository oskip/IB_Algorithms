# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
#
# Example:
# given array S = {-1 2 1 -4},
# and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
#

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        if len(A) < 3: return
        A = sorted(A)
        bestVal = float("inf")
        best = 0
        for i in range(0, len(A)-2):
            j = i+1
            k = len(A)-1
            while j < k:
                currVal = abs(A[j]+A[k]+A[i]-B)
                if bestVal > currVal:
                    bestVal = currVal
                    best = A[j]+A[k]+A[i]
                if A[j]+A[k]+A[i] == B: return A[i]+A[j]+A[k]
                elif A[j]+A[k]+A[i] > B:
                    k -= 1
                else:
                    j += 1
        return best


print Solution().threeSumClosest([ 2, 1, -9, -7, -8, 2, -8, 2, 3, -8 ], -1)
