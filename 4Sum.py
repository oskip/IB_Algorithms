# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
#  Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
# The solution set must not contain duplicate quadruplets.
# Example :
# Given array S = {1 0 -1 0 -2 2}, and target = 0
# A solution set is:
#
#     (-2, -1, 1, 2)
#     (-2,  0, 0, 2)
#     (-1,  0, 0, 1)
# Also make sure that the solution set is lexicographically sorted.
# Solution[i] < Solution[j] iff Solution[i][0] < Solution[j][0] OR (Solution[i][0] == Solution[j][0] AND ... Solution[i][k] < Solution[j][k])


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        A = sorted(A)
        sums = {}
        res = []
        for i,a in enumerate(A):
            for b in A[i+1:]:
                if B-(a+b) in sums:
                    for el in sums[B-(a+b)]:
                        c,d = el
                        r = sorted([a,b,c,d])
                        if r not in res: res.append(r)
                if a+b not in sums: sums[a+b] = []
                if (a,b) not in sums[a+b] and (b,a) not in sums[a+b]:
                    sums[a+b].append((a,b))
        return sorted(res)

print Solution().fourSum([1,0,-1,0,-2,2],0)