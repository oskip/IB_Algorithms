import math


class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        if int(A) < 2: return 0
        logVal = math.log(int(A), 2)
        if int(A) - (2 ** int(logVal)) == 0: return 1
        else: return 0


print Solution().power("5070602400912917605986812821505")
