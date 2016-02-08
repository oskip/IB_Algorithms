# You are given an array of N integers, A1, A2, ..., AN and an integer K. Return the of count of distinct numbers in all windows of size K.
#
# Formally, return an array of size N-K+1 where i'th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+k-1.
#
# Note:
# - If K > N, return empty array.
#
# For example,
#
# A=[1, 2, 1, 3, 4, 3] and K = 3
#
# All windows of size K are
#
# [1, 2, 1]
# [2, 1, 3]
# [1, 3, 4]
# [3, 4, 3]
#
# So, we return an array [2, 3, 3, 2].


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        if len(A) < B: return []
        start = 0
        stop = B-1
        window = {}
        currCt = 0
        res = []
        for i in range(0,B):
            if A[i] not in window:
                window[A[i]] = 1
                currCt += 1
            else: window[A[i]] += 1
        res.append(currCt)

        while stop < len(A)-1:
            window[A[start]] -= 1
            if window[A[start]] == 0:
                currCt -= 1
                del window[A[start]]
            start += 1
            stop += 1
            if A[stop] not in window:
                window[A[stop]] = 1
                currCt += 1
            else: window[A[stop]] += 1
            res.append(currCt)
        return res

print Solution().dNums([1,2,5,3,1,2,4,1,1,2,9,4,3,2,6,1,2,7,5,7], 8)