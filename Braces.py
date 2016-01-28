# Write a program to validate if the input string has redundant braces?
# Return 0/1
#  0 -> NO 1 -> YES
#
# Input will be always a valid expression
#
# and operators allowed are only + , * , - , /
#
# Example:
#
# ((a+b)) has redundant braces so answer will be 1
# (a + (a + b)) doesn't have have any redundant braces so answer will be 0


class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        brackets = []
        wasOp = False
        wasNum = False
        prevB = ""
        for a in A:
            if a in ['+','-','*','/']: wasOp = True
            elif '0'<=a<='9' or 'a'<=a<='z' or 'A'<=a<='Z': wasNum = True
            elif a == '(':
                if prevB == "": prevB = a
                else: brackets.append((wasOp&wasNum,prevB))
                wasOp = wasNum = False
            elif a == ')':
                if prevB == "(":
                    if not wasOp&wasNum: return 1
                    prevB = ""
                elif len(brackets) > 0:
                    b,c = brackets.pop()
                    if not (b | wasOp&wasNum): return 1
                else: return
                wasOp = wasNum = False
        return 0

print Solution().braces("a*(a+b)*c+(a*(a-(c*c+(d*e))+f*(f+d))-e)")