# Find the kth smallest element in an unsorted array of non-negative integers.
#
# Definition of kth smallest element
#
#  kth smallest element is the minimum possible n such that there are atleast k elements in the array <= n.
# In other words, if the array A was sorted, then A[k - 1] ( k is 1 based, while the arrays are 0 based )
# NOTE
# You are not allowed to modify the array ( The array is read only ).
# Try to do it using constant extra space.
#
# Example:
#
# A : [2 1 4 3 2]
# k : 3
#
# answer : 2

import heapq as heapq


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, k):
        arr = []
        for a in A:
            heapq.heappush(arr, a)
        print heapq.nsmallest(k, arr)[-1]

Solution().kthsmallest([3,8,7,1,3,14],2)

