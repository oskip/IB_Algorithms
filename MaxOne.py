# You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.
# Find the position of zeros which when flipped will produce maximum continuous series of 1s.
#
# For this problem, return the indices of maximum continuous series of 1s in order.
#
# Example:
#
# Input :
# Array = {1 1 0 1 1 0 0 1 1 1 }
# M = 1
#
# Output :
# [0, 1, 2, 3, 4]
#
# If there are multiple possible solutions, return the sequence which has the minimum start index.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        start = 0
        stop = 0
        gaps = B
        maxL = 0
        result = []
        for b in A:
            if b == 0: gaps -= 1
            stop += 1
            if gaps < 0:
                wasZero = False
                while not wasZero:
                    if A[start] == 0: wasZero = True
                    start += 1
                gaps += 1
            elif stop-start > maxL:
                maxL = stop-start
                result = range(start, stop)
        if stop-start > maxL:
            result = range(start, stop)
        return result


print Solution().maxone([0, 1, 1, 1], 0)


