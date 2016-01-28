# Given two numbers represented as strings, return multiplication of the numbers as a string.
#
#  Note: The numbers can be arbitrarily large and are non-negative.
# Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer.
# For example,
# given strings "12", "10", your answer should be “120”.
#
# NOTE : DO NOT USE BIG INTEGER LIBRARIES ( WHICH ARE AVAILABLE IN JAVA / PYTHON ).
# We will retroactively disqualify such submissions and the submissions will incur penalties.


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        strs = []
        result = ""
        for i in reversed(range(0,len(B))):
            nb = B[i]
            string = "0"*(len(B)-(i+1))
            carry = 0
            for j in reversed(range(0,len(A))):
                na = A[j]
                product = int(na)*int(nb)+carry
                string = str(product%10) + string
                carry = product/10
            if carry > 0: string = str(carry) + string
            strs.append(string)
        maxLen = max([len(s) for s in strs])
        strs = [ e.zfill(maxLen) for e in strs]
        carry = 0
        for i in reversed(range(0, maxLen)):
            product = carry
            for string in strs:
                product += int(string[i])
            result = str(product % 10) + result
            carry = product/10
        if carry > 0: result = str(carry) + result
        result = result.lstrip("0")
        return result if len(result) > 0 else "0"

print Solution().multiply("9999", "0")
