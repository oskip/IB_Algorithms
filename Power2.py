class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        if A == 0:
            return
        if A == 1: return True

        baseFactor = 0
        for i in xrange(2, int(A**0.5)+1):
            if A % i == 0:
                j = 1
                val = i
                while val < A:
                    val = i**j
                    j += 1
                    if val == A: return True
        return False


print Solution().isPower(700227073)