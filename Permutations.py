# Given a collection of numbers, return all possible permutations.
#
# Example:
#
# [1,2,3] will have the following permutations:
#
# [1,2,3]
# [1,3,2]
# [2,1,3]
# [2,3,1]
# [3,1,2]
# [3,2,1]
#  NOTE
# No two entries in the permutation sequence should be the same.
# For the purpose of this problem, assume that all the numbers in the collection are unique.


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        self.res = []
        A = sorted(A)
        for a in A:
            rem = [e for e in A if e != a]
            self.nextPermute(rem, [a])
        return self.res

    def nextPermute(self, A, curr):
        if len(A) == 0: self.res.append(curr)
        for a in A:
            rem = [e for e in A if e != a]
            self.nextPermute(rem, curr+[a])
