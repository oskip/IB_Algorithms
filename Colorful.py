# For Given Number N find if its COLORFUL number or not
#
# Return 0/1
#
# COLORFUL number:
#
# A number can be broken into different sub-sequence parts.
# Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
# And this number is a COLORFUL number, since product of every digit of a sub-sequence are different
# Example:
#
# N = 23
# 2 3 23
# 2 -> 2
# 3 -> 3
# 23 -> 6
# this number is a COLORFUL number since product of every digit of a sub-sequence are different.
#
# Output : 1

class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        products = {}
        A = str(A)
        if len(A) < 2: return 1
        for size in range(1, len(A)+1):
            start = 0
            stop = size
            while stop <= len(A):
                product = 1
                for c in A[start:stop]: product *= int(c)
                if product in products: return 0
                else: products[product] = True
                start += size
                stop += size
        return 1

print Solution().colorful(78034854)