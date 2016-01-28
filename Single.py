class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        result = 0
        to = 0
        maxA = max(A)
        while maxA > 0:
            maxA >>=1
            to += 1
        for b in range(0, to):
            ct0 = 0
            ct1 = 0
            for a in A:
                if (a >> b) & 1:
                    ct1 += 1
                else: ct0 += 1
            if ct1%2 == 1:
                result += 1 << b
        return result
