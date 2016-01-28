# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.
#
# For example, given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"
# Make sure the returned list of strings are sorted.


class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        self.res = []
        O = A
        C = A
        self.generate("",O,C)
        return self.res

    def generate(self,curr,O,C):
        if O == 0 and C == 0 and self.isValid(curr): self.res.append(curr)
        if O > 0: self.generate(curr+"(",O-1,C)
        if C > 0: self.generate(curr+")",O,C-1)

    def isValid(self, S):
        stack = []
        for s in S:
            if s == "(": stack.append(s)
            elif s == ")":
                if len(stack) > 0 and stack[-1] == "(": stack.pop()
                else: return False
        return len(stack) == 0

print Solution().generateParenthesis(12)