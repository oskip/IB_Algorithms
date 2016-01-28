# Remove Duplicates from Sorted Array
#
# Given a sorted array, remove the duplicates in place such that each element appear atmost twice and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# Note that even though we want you to return the new length, make sure to change the original array as well in place
#
# For example,
# Given input array A = [1,1,1,2],
#
# Your function should return length = 3, and A is now [1,1,2].

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 3: return len(A)
        pIndex = 0
        for i in range(0, len(A)):
            A[pIndex] = A[i]
            if i < len(A)-2 and A[i] == A[i+1] == A[i+2]: continue
            else: pIndex += 1
        A = A[:pIndex]
        print A
        return len(A)


print Solution().removeDuplicates([ 0, 1, 1, 2, 2, 3, 3, 3, 4])