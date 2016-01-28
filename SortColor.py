# Given an array with n objects colored red, white or blue,
# sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: Using library sort function is not allowed.
#
# Example :
#
# Input : [0 1 2 0 1 2]
# Modify array so that it becomes : [0 0 1 1 2 2]


class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        ct = [0]*3
        for a in A: ct[a]+=1
        i = 0
        for j, c in enumerate(ct):
            while c > 0:
                A[i] = j
                c -= 1
                i += 1
        return A
