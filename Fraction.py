# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# Example :
#
# Given numerator = 1, denominator = 2, return "0.5"
# Given numerator = 2, denominator = 1, return "2"
# Given numerator = 2, denominator = 3, return "0.(6)"

# ŹLE!!!!!!!!!!!!!!

from decimal import *
class Solution:
    # @param numerator : integer
    # @param denominator : integer
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0: return
        if numerator == 0: return 0
        getcontext().prec = 1000
        n = Decimal(numerator)
        d = Decimal(denominator)
        res = '{:f}'.format(n/d)
        if "." not in res: return res
        lastPosOf = [-1] * 10
        decs = res[res.index(".")+1:]
        for i, s in enumerate(decs):
            if lastPosOf[int(s)] != -1:
                hypRepeat = decs[lastPosOf[int(s)]:i]
                hypRepeatStart = i-len(hypRepeat)
                if hypRepeat == decs[i:i+len(hypRepeat)]:
                    j = i+len(hypRepeat)
                    repeat = True
                    while j+len(hypRepeat) < len(decs):
                        if decs[j:j+len(hypRepeat)] != hypRepeat:
                            repeat = False
                            break
                        j += len(hypRepeat)
                    if repeat:
                        return res[0:res.index(".")]+"."+decs[0:hypRepeatStart]+"("+decs[hypRepeatStart:i]+")"
            else: lastPosOf[int(s)] = i
        return res

print Solution().fractionToDecimal(87,22)
