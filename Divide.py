# Divide two integers without using multiplication, division and mod operator.
#
# Return the floor of the result of the division.
#
# Example:
#
# 5 / 2 = 2
# Also, consider if there can be overflow cases. For overflow case, return INT_MAX.


class Solution:
    # @param dividend : integer
    # @param divisor : integer
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor == 0 and dividend > 0: return 2 ** 31 - 1
        if divisor == 0 and dividend < 0: return -(2 ** 31)
        if dividend == divisor: return 1

        minusFlag = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0): minusFlag = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor > dividend: return 0
        shiftedDivisor = divisor
        posFlag = 1
        result = 0

        while shiftedDivisor <= dividend:
            shiftedDivisor <<= 1
            posFlag <<= 1

        posFlag >>= 1
        shiftedDivisor >>= 1

        while posFlag > 0:
            if dividend >= shiftedDivisor:
                dividend -= shiftedDivisor
                result |= posFlag
            posFlag >>= 1
            shiftedDivisor >>= 1

        if minusFlag: result = -result
        return min(max(result, -(2 ** 31)), 2 ** 31 - 1)


print Solution().divide(4, 5)
