# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# PROBLEM APPROACH :
#
# Complete solution in hints.


class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        openStack = []
        for a in A:
            if a in ["{", "[", "("]: openStack.append(a)
            elif a == "}":
                if len(openStack) < 1 or openStack.pop() != "{": return 0
            elif a == "]":
                if len(openStack) < 1 or openStack.pop() != "[": return 0
            elif a == ")":
                if len(openStack) < 1 or openStack.pop() != "(": return 0
        return 1 if len(openStack) == 0 else 0

print Solution().isValid("{({{(([]))}})}")