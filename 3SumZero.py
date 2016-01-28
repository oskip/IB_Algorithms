# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
#  Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets. For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
# (-1, 0, 1)
# (-1, -1, 2)

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A = sorted(A)
        n = len(A)
        result = []
        for i in range(0, n-2):
            j = i + 1
            k = n - 1
            while j < k:
                sumIn = A[i]+A[j]+A[k]
                if sumIn == 0:
                    if [A[i], A[j], A[k]] not in result: result.append([A[i], A[j], A[k]])
                    k -= 1
                elif sumIn > 0: k -= 1
                elif sumIn < 0: j += 1
        return result

print Solution().threeSum([ -1, -4, -5, -19, 20, 32, 23, 11, 59, -31, -2, 0, 0, 0, 0, -1, 12, 4, 6, -9, 3, 13, -11])