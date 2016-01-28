# The gray code is a binary numeral system where two successive values differ in only one bit.
#
# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
#
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
#
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# There might be multiple gray code sequences possible for a given n.
# Return any such sequence.


class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        self.res = [0]*2**A
        for level in range(A):
            factor = 2**level
            i = 0
            while i < 2**A:
                if (i/factor)%4 == 0 or (i/factor)%4 == 3: self.res[i] += 0 << level
                if (i/factor)%4 == 1 or (i/factor)%4 == 2: self.res[i] += 1 << level
                i += 1
        return self.res

print Solution().grayCode(5)