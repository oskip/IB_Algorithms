class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        ct = 0
        while A > 0:
            if A % 2 == 1: ct += 1
            A >>= 1
        return ct


print Solution().numSetBits(0)
