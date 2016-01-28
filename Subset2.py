# Given a collection of integers that might contain duplicates, S, return all possible subsets.
#
#  Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# The subsets must be sorted lexicographically.
# Example :
# If S = [1,2,2], the solution is:
#
# [
# [],
# [1],
# [1,2],
# [1,2,2],
# [2],
# [2, 2]
# ]


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        self.A = sorted(A)
        self.res = [[]]
        self.getSubset([], 0)
        return self.res

    def getSubset(self, curr, index):
        for i in range(index,len(self.A)):
            tmpCurr = curr+[self.A[i]]
            if tmpCurr not in self.res: self.res.append(tmpCurr)
            self.getSubset(tmpCurr, i+1)
