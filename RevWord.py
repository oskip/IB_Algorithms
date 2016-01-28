# Given an input string, reverse the string word by word.
#
# Example:
#
# Given s = "the sky is blue",
#
# return "blue is sky the".
#
# A sequence of non-space characters constitutes a word.
# Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
# If there are multiple spaces between words, reduce them to a single space in the reversed string.


class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        i = 0
        j = len(A)-1
        while A[i] == ' ': i += 1
        while A[j] == ' ': j -= 1
        A = A[0:j+1]
        wordStart = i
        result = ""
        while i < len(A):
            if A[i] == " ":
                if wordStart > -1:
                    result = " " + A[wordStart:i] + result
                    wordStart = -1
            elif wordStart == -1:
                wordStart = i
            i += 1

        result = A[wordStart:len(A)] + result
        return result
