class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A < 0: return
        if 0 <= A < 2: return A

        return self.sqrtSearch(1, A/2, A)

    def sqrtSearch(self, start, stop, A):
        while start <= stop:
            middle = (start+stop)/2
            if middle**2 <= A < (middle+1)**2:
                return middle
            elif middle**2 > A:
                stop = middle-1
            else:
                start = middle+1
            return self.sqrtSearch(start, stop, A)

print Solution().sqrt(4)


