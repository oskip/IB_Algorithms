class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if d == 1: return 0

        rem = x % d
        p = 1
        while n > 0:
            if n % 2 == 1:
                p *= rem
                p %= d
            n /= 2
            rem = rem**2 % d

        return p


print Solution().pow(71045970, 41535484, 64735492)


