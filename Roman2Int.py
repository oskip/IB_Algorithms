# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.
#
# Read more details about roman numerals at Roman Numeric System
#
# Example :
#
# Input : "XIV"
# Return : 14
# Input : "XX"
# Output : 20


class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        if len(A) < 1: return 0
        romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D":500, "M": 1000}
        value = 0
        maxVal = 0
        for c in reversed(A):
            if c not in romanDict: return 0
            tmpVal = romanDict[c]
            if tmpVal < maxVal:
                value -= tmpVal
            else:
                value += tmpVal
                maxVal = tmpVal
        return value

print Solution().romanToInt("MMCDLXXV")