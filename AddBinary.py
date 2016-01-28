# Given two binary strings, return their sum (also a binary string).
#
# Example:
#
# a = "100"
#
# b = "11"
# Return a + b = "111".

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        maxLen = max(len(A),len(B))
        A = A.rstrip().zfill(maxLen)
        B = B.rstrip().zfill(maxLen)
        carry = 0
        result = ""
        i = maxLen-1
        while i >= 0 or carry > 0:
            bit = carry
            if i >= 0: bit += int(A[i])+int(B[i])
            if bit < 2:
                carry = 0
                result = str(bit) + result
            elif bit == 2:
                carry = 1
                result = "0" + result
            elif bit == 3:
                carry = 1
                result = "1" + result
            i -= 1
        return result