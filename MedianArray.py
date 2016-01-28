class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        n = len(A)-1
        m = len(B)-1
        if n < 0:
            return self.median(B)
        elif m < 0:
            return self.median(A)
        start = 0
        stop = n
        while start <= stop:
            i = (start+stop)/2
            j = (n+m)/2-i
            if j > m:
                start = i
                continue
            elif j < 0:
                stop = i
                continue
            if (j == m and i < n and B[j] <= A[i+1]) or (i ==n and j < m and A[i] <= B[j+1]) or (j < m and i < n and B[j] <= A[i+1] and A[i] <= B[j+1]):
                if (n+m)%2 == 1:
                    return max(B[j], A[i])
                else:
                    res = (B[j]+A[i])/2
                    return res
            elif i < n and B[j] > A[i+1]:
                start = i
            elif j < m and A[i] > B[j+1]:
                stop = i
        return 0

    def median(self, A):
        n = len(A)
        if n%2 == 0: return (A[n/2] + A[n/2-1])/2
        else: return A[n/2]


print Solution().findMedianSortedArrays([ -43, -25, -18, -15, -10, 9, 39, 40 ],[ -2 ])
