# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Here are few examples.
#
# [1,3,5,6], 5 -> 2
# [1,3,5,6], 2 -> 1
# [1,3,5,6], 7 -> 4
# [1,3,5,6], 0 -> 0


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        n = len(A)-1
        start = 0
        stop = n+1
        if A[0] >= B: return 0
        if A[n] <= B: return n+1
        while start <= stop:
            middle = (start+stop)/2
            if A[middle] == B or (A[middle-1] < B <= A[middle]):
                return middle
            elif A[middle] > B:
                stop = middle-1
            else:
                start = middle+1

print Solution().searchInsert([1,3,5,6], 47)