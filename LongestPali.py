# Given a string S, find the longest palindromic substring in S.
#
# Substring of string S:
#
# S[i...j] where 0 <= i <= j < len(S)
#
# Palindrome string:
#
# A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.
#
# Incase of conflict, return the substring which occurs first ( with the least starting index ).
#
# Example :
#
# Input : "aaaabaaa"
# Output : "aaabaaa"


class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        if len(A) < 2: return A
        if len(A) == 2 and A[0] == A[1]: return A
        if len(A) == 3 and A[0] == A[1] != A[2]: return A[0:2]
        longestPali = A[0]
        for i in xrange(1,len(A)-1):
            start = i-1
            stop = i+1
            pali = ""
            while start >= 0 and stop < len(A):
                if A[start] == A[stop]:
                    pali = A[start:stop+1]
                    start -=1
                    stop += 1
                else: break
            if len(pali) > len(longestPali): longestPali = pali
            if A[i] == A[i+1]:
                start = i-1
                stop = i+2
                pali = A[i:i+2]
                while start >= 0 and stop < len(A):
                    if A[start] == A[stop]:
                        pali = A[start:stop+1]
                        start -=1
                        stop += 1
                    else: break
            if len(pali) > len(longestPali): longestPali = pali
        return longestPali

print Solution().longestPalindrome("vvv")
