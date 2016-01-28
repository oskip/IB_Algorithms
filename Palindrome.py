# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Example:
#
# "A man, a plan, a canal: Panama" is a palindrome.
#
# "race a car" is not a palindrome.
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

import re

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        A = re.sub(r"[^A-Za-z0-9]", '', A).lower()
        return A == A[::-1]

print Solution().isPalindrome("A man, a plan, a canal: Panama")