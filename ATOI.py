# Please Note:
#
# There are certain questions where the interviewer would intentionally frame the question vague.
# The expectation is that you will ask the correct set of clarifications or state your assumptions before you jump into coding.
#
# Implement atoi to convert a string to an integer.
#
# Example :
#
# Input : "9 2704"
# Output : 9
# Note: There might be multiple corner cases here. Clarify all your doubts using "See Expected Output".
#
#  Questions: Q1. Does string contain whitespace characters before the number?
# A. Yes Q2. Can the string have garbage characters after the number?
# A. Yes. Ignore it. Q3. If no numeric character is found before encountering garbage characters, what should I do?
# A. Return 0. Q4. What if the integer overflows?
# A. Return INT_MAX if the number is positive, INT_MIN otherwise.
# Warning : DO NOT USE LIBRARY FUNCTION FOR ATOI.
# If you do, we will disqualify your submission retroactively and give you penalty points.


class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        val = 0
        i = 0
        minusFlag = False
        plusFlag = False
        for c in A:
            if i == 0 and c == '-':
                if not minusFlag:
                    minusFlag = True
                    continue
                else: return 0
            if i == 0 and c == '+':
                if not plusFlag:
                    plusFlag = True
                    continue
                else: return 0
            if i == 0 and c == " " and not (minusFlag or plusFlag): continue
            if 48 <= ord(c) <= 57:
                val = val*10+(ord(c)-48)
            else: return self.returnVal(val, minusFlag)
            i += 1
        return self.returnVal(val, minusFlag)

    def returnVal(self, val, minusFlag):
        val = -val if minusFlag else val
        val = min(val, 2147483647)
        val = max(val, -2147483648)
        return val