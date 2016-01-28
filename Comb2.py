# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
#  Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
# The solution set must not contain duplicate combinations.
# Example :
#
# Given candidate set 10,1,2,7,6,1,5 and target 8,
#
# A solution set is:
#
# [1, 7]
# [1, 2, 5]
# [2, 6]
# [1, 1, 6]


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A = sorted(A)
        A = [a for a in A if a <= B]
        res = []
        for i, a in enumerate(A):
            s = a
            if s == B: res.append([B])
            else: self.combIter(res, [a], s, i, A, B)
        return res

    def combIter(self, res, curr, s, index, A, B):
        if s > B: return
        for i in range(index+1,len(A)):
            tmpCurr = [c for c in curr]
            tmpCurr.append(A[i])
            s = sum(tmpCurr)
            if s == B and tmpCurr not in res: res.append(tmpCurr)
            self.combIter(res, tmpCurr, s, i, A, B)


print Solution().combinationSum([ 17, 8, 17, 20, 20, 18, 14, 15, 20, 3 ],14)