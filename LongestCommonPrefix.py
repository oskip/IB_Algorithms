# Write a function to find the longest common prefix string amongst an array of strings.
#
# Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.
#
# As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".
#
# Given the array of strings, you need to find the longest S which is the prefix of ALL the strings in the array.
#
# Example:
#
# Given the array as:
#
# [
#
#   "abcdefgh",
#
#   "aefghijk",
#
#   "abcefgh"
# ]
# The answer would be "a".

class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        if len(A) == 0: return ""
        if len(A) == 1: return A[0]

        prefix = ""
        for i in xrange(0, len(A[0])):
            inAll = True
            for string in A:
                if i >= len(string) or string[i] != A[0][i]:
                    inAll = False
                    break
            if inAll: prefix += A[0][i]
            else: return prefix
        return prefix

