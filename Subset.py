# Given a set of distinct integers, S, return all possible subsets.
#
#  Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# Also, the subsets should be sorted in ascending ( lexicographic ) order.
# Example :
#
# If S = [1,2,3], a solution is:
#
# [
#   [],
#   [1],
#   [1, 2],
#   [1, 2, 3],
#   [1, 3],
#   [2],
#   [2, 3],
#   [3],
# ]


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A = sorted(A)
        res = [[]]
        for i in range(len(A)):
            res.append([A[i]])
            self.subsetsIter(res, [A[i]], i, 2, A)
        return res

    def subsetsIter(self, res, curr, lastIndex, level, A):
        if level > len(A): return
        for j in range(lastIndex+1,len(A)):
            tmpcurr = [c for c in curr]
            tmpcurr.append(A[j])
            res.append(tmpcurr)
            self.subsetsIter(res, tmpcurr, j, level+1, A)


# Ze strony
class Solution2:
    def subsets(self, s):
        s.sort()
        r = [[]]
        for e in s:
            r += [x+[e] for x in r]
        return sorted(r)


print Solution().subsets([1,4,2,5])
print Solution2().subsets([1,4,2,5])
