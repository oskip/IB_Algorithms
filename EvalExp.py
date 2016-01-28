# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Examples:
#
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        numStack = []
        for a in A:
            if a in ["+", "-", "*", "/"]:
                if len(numStack) < 2: return
                q = numStack.pop()
                p = numStack.pop()
                if a == "+": numStack.append(p+q)
                elif a == "-": numStack.append(p-q)
                elif a == "*": numStack.append(p*q)
                elif a == "/": numStack.append(p/q)
            else: numStack.append(int(a))
        return numStack.pop()

print Solution().evalRPN(["2","7","+","3","/","14","3","-","4","*","+","2","/"])