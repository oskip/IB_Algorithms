# The count-and-say sequence is the sequence of integers beginning as follows:
#
# 1, 11, 21, 1211, 111221, ...
# 1 is read off as one 1 or 11.
# 11 is read off as two 1s or 21.
#
# 21 is read off as one 2, then one 1 or 1211.
#
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.
#
# Example:
#
# if n = 2,
# the sequence is 11.

class Solution:
    # @param A : integer
    # @return a stringsł
    def countAndSay(self, A):
        if A < 1: return ""
        if A == 1: return "1"
        i = 1
        seq = "1"
        while i < A:
            newSeq = ""
            currNumCt = 0
            lastNum = seq[0]
            for num in seq:
                if num == lastNum: currNumCt += 1
                else:
                    newSeq += str(currNumCt)+lastNum
                    lastNum = num
                    currNumCt = 1
            newSeq += str(currNumCt)+lastNum
            i += 1
            seq = newSeq
        return seq
