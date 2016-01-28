# Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values in the array
#
# Note:
#
# 1) Return the indices `A1 B1 C1 D1`, so that
#   A[A1] + A[B1] = A[C1] + A[D1]
#   A1 < B1, C1 < D1
#   A1 < C1, B1 != D1, B1 != C1
#
# 2) If there are more than one solutions,
#    then return the tuple of values which are lexicographical smallest.
#
# Assume we have two solutions
# S1 : A1 B1 C1 D1 ( these are values of indices int the array )
# S2 : A2 B2 C2 D2
#
# S1 is lexicographically smaller than S2 iff
#   A1 < A2 OR
#   A1 = A2 AND B1 < B2 OR
#   A1 = A2 AND B1 = B2 AND C1 < C2 OR
#   A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
# Example:
#
# Input: [3, 4, 7, 1, 2, 9, 8]
# Output: [0, 2, 3, 5] (O index)
# If no solution is possible, return an empty list.
#


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        dic = {}
        r = []
        for a in range(len(A)):
            for b in range(a,len(A)):
                if a == b: continue
                if A[a]+A[b] not in dic: dic[A[a]+A[b]] = (a,b)
                elif dic[A[a]+A[b]][0] > a or (dic[A[a]+A[b]] == a and dic[A[a]+A[b]][1] > b):
                    dic[A[a]+A[b]] = (a,b)
        for c in range(len(A)):
            for d in range(c,len(A)):
                if A[c]+A[d] not in dic: continue
                else:
                    (a,b) = dic[A[c]+A[d]]
                    if a != c and b != c and b != d and c != d:
                        if len(r) == 0: r = [a,b,c,d]
                        elif a < r[0] or (a == r[0] and b < r[1]) or (a == r[0] and b == r[1] and c < r[2]) or (a == r[0] and b == r[1] and c == r[2] and d < r[3]):
                            r = [a,b,c,d]
        return r

print Solution().equal([3, 4, 7, 1, 2, 9, 8])