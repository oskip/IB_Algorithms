class Solution:
    # @param A : list of integers
    # @return an integer
    def cntMatrix(self, A):

        n = len(A)
        d = 1
        res = 0
        mod = (10**9+7)
        while d <= n:
            if n%d == 0:
                if self.isSorted(A,d):
                    curr = 1
                    for _ in range(n/d):
                        curr2 = 1
                        for j in range(1,d+1): curr2 *= j
                        curr *= curr2
                    res += curr
            d += 1
        return max(res,1)

    def isSorted(self, A, d):
        i = 1
        while i < len(A):
            if A[i] < A[i-1]: return False
            i += 1
            if i%d==0: i += 1
        return True

mat = range(1,51)
print Solution().cntMatrix(mat)

784534666