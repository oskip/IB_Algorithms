# Find the largest continuous sequence in a array which sums to zero.
#
# Example:
#
#
# Input:  {1 ,2 ,-2 ,4 ,-4}
# Output: {2 ,-2 ,4 ,-4}
#
#  NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        s = 0
        sums = []
        sumsDic = {}
        solution = []
        for a in A:
            sums.append(s)
            s += a
        sums.append(s)
        if sums[-1] == 0: return A
        for i, e in enumerate(sums):
            if e in sumsDic:
                j = sumsDic[e]
                if i-j > len(solution): solution = A[j:i]
            else: sumsDic[e] = i
        return solution

print Solution().lszero([1,2,-3,3])