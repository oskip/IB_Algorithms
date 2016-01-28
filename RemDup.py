# Remove duplicates from Sorted Array
# Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.
#
# Note that even though we want you to return the new length, make sure to change the original array as well in place
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
#  Example:
# Given input array A = [1,1,2],
# Your function should return length = 2, and A is now [1,2].


class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 2: return len(A)
        i = 1
        pIndex = 1
        while i < len(A):
            if A[i] != A[i-1]:
                A[pIndex] = A[i]
                pIndex += 1
            i += 1
        A = A[:pIndex]
        return pIndex

print Solution().removeDuplicates([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ])