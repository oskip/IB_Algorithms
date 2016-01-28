# Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.
#
# Make sure the combinations are sorted.
#
# To elaborate,
# 1. Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
# 2. Entries should be sorted within themselves.
#
# Example :
# If n = 4 and k = 2, a solution is:
#
# [
#   [1,2],
#   [1,3],
#   [1,4],
#   [2,3],
#   [2,4],
#   [3,4],
# ]
#


class Solution:
    # @param n : integer
    # @param k : integer
    # @return a list of list of integers
    def combine(self, n, k):
        if k == 1: return [[e]for e in range(1,n+1)]
        firsts = range(1,n-k+2)
        res = []
        for f in firsts:
            self.newCombine(res, 1, [f], n, k)
        return res

    def newCombine(self, arr, level, curr, n, k):
        for i in range(curr[-1]+1,n-(k-level)+2):
            cur = [c for c in curr]
            cur.append(i)
            if len(cur) == k: arr.append(cur)
            else: self.newCombine(arr, level+1, cur, n, k)

print Solution().combine(10,2)