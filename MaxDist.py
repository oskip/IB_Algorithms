class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A) == 0:
            return -1

        Lmin = []
        Rmax = []
        minVal = float('inf')
        maxVal = float('-inf')
        for i, val in enumerate(A):
            minVal = min(minVal, val)
            Lmin.append(minVal)
        for i in reversed(xrange(0, len(A))):
            maxVal = max(maxVal, A[i])
            Rmax.append(max(maxVal, A[i]))
        Rmax.reverse()
        i = j = 0
        best = 0
        while i < len(Lmin) and j < len(Rmax):
            if Rmax[j]-Lmin[i] >= 0:
                best = max(best, j-i)
                if j < len(Rmax): j += 1
                else: i += 1
            else:
                i = min(len(Lmin), i+1)
        return best


Solution().maximumGap([3, 5, 4, 2])