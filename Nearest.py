# Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.
#
# More formally,
#
# G[i] for an element A[i] = an element A[j] such that
#     j is maximum possible AND
#     j < i AND
#     A[j] < A[i]
# Elements for which no smaller element exist, consider next smaller element as -1.
#
# Example:
#
# Input : A : [4, 5, 2, 10]
# Return : [-1, 4, -1, 2]
#
# Example 2:
#
# Input : A : [3, 2, 1]
# Return : [-1, -1, -1]


class Solution:
    # @param arr : list of integers
    # @return a list of integers
    def prevSmaller(self, arr):
        stack = []
        res = [-1]*len(arr)
        stack.append(arr[0])
        for i in range(1,len(arr)):
            while len(stack) > 0 and stack[-1] >= arr[i]: stack.pop()
            if len(stack) > 0: res[i] = stack[-1]
            stack.append(arr[i])
        return res

print Solution().prevSmaller([ 39, 27, 11, 4, 24, 32, 32, 1 ])