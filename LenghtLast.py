# coding=utf-8
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
# Given s = "Hello World",
#
# return 5 as length("World") = 5.
#
# Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once.


class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        if A == "": return 0
        i = 0
        for a in reversed(A):
            if a == ' ' and i == 0: continue
            if a == ' ': return i
            i += 1
        return i

print Solution().lengthOfLastWord("a wtan   ")

