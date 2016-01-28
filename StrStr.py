# Please Note:
#
# Another question which belongs to the category of questions which are intentionally stated vaguely.
# Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.
#
# Implement strStr().
#
#  strstr - locate a substring ( needle ) in a string ( haystack ).
# Try not to use standard library string functions for this question.
#
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
#  NOTE: Good clarification questions:
# What should be the return value if the needle is empty?
# What if both haystack and needle are empty?
# For the purpose of this problem, assume that the return value should be -1 in both cases.


class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        if len(haystack) == 0 or len(needle) == 0:
            return -1
        matcher = ""
        for i, c in enumerate(haystack):
            matcher += c
            if len(matcher) > len(needle):
                matcher = matcher[1:]
            if matcher == needle:
                return i - (len(needle)-1)
        return -1

