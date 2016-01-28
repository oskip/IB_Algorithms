class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        i = 1
        result = 0
        while 5**i <= A:
            result += (A/(5**i))
            i += 1
        return result

bigNum = 1000000000000098797979790000000
result = Solution().trailingZeroes(bigNum)
print result, result-0.25*bigNum